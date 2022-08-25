import webbrowser


urls = ['Larreamarcadigital.cl', 'ograma.cl', 'Aimpresores.cl', 'dimacofi.cl']
url = 'Larreamarcadigital.cl'
# MacOS
chrome_path = 'open -a /Applications/Firefox.app %s'

webbrowser.get(chrome_path).open(url)