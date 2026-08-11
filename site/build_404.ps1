$content = [System.IO.File]::ReadAllText('c:\Users\Admin\Documents\Projetos\code-house\index.html', [System.Text.Encoding]::UTF8)
$newMain = '<main><section class="hero" style="min-height: 70vh; display: flex; align-items: center; justify-content: center; text-align: center;"><div class="container"><p class="eyebrow">// 404</p><h1 class="section-title" style="margin-bottom: 1rem;">Sistema não encontrado</h1><p class="process-desc" style="margin-bottom: 2rem;">Parece que você acessou um link quebrado ou a página foi movida.</p><a href="index.html" class="btn btn-solid">Voltar para o início</a></div></section></main>'
$content = [System.Text.RegularExpressions.Regex]::Replace($content, '(?s)<main>.*?</main>', $newMain)
$content = $content -replace '<title>.*?</title>', '<title>404 — Sistema não encontrado | Code House</title>'
[System.IO.File]::WriteAllText('c:\Users\Admin\Documents\Projetos\code-house\404.html', $content, [System.Text.Encoding]::UTF8)
