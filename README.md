# Workshop 2.6 - CI/CD

Projeto preparado para a atividade de integracao e entrega continua.

## Execucao local

```powershell
python -m pip install -r requirements.txt
python -m flake8 src/ tests/ --max-line-length=100
python -m pytest tests/ -v --html=report/index.html --self-contained-html
```

O workflow `.github/workflows/ci.yml` executa o lint e os testes em Pull
Requests. O job `deploy` so publica o relatorio no GitHub Pages depois de um
push na branch `main` e apos o job de testes passar.
