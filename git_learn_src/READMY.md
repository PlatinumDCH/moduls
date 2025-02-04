# Git Cheat Sheet

## Настройки
```sh
git config --global user.name 'example name'
git config --global user.email 'example email'
```

### Установка редактора для коммитов (VSCode)
```sh
git config --global core.editor "code --wait"
```

---

## Поиск в справке Git
```sh
/<searching element>   # Найти элемент
n                      # Следующее вхождение
Shift + n              # Предыдущее вхождение
```

---

## Создание Pull Request
```sh
git switch -c 'nameNewBranch'  # Создание новой ветки
# Работаем в ветке

git add .
git commit -m "Commit message"
git push origin 'createdNameNewBranch'  # Создание Pull Request
```

---

## Визуализация
```sh
git log --decorate --graph --all  # Полная информация о коммитах
```

---

## Основные команды
### Работа с ветками
```sh
git clone https://linkRepo     # Клонирование репозитория

git checkout 'nameBranch'      # Переключение на ветку

git switch <nameBranch>        # Переключение на ветку (альтернатива checkout)

git pull origin 'nameBranch'   # Получение данных с GitHub

git checkout -b 'nameNewBranch'  # Создание новой ветки и переход в неё

git switch -c 'nameBranch'     # Создание и переключение на новую ветку

git branch -m <old> <new>      # Переименование ветки

git branch -D <nameBranch>     # Удаление ветки в локальном репо

git push origin --delete <nameBranch>  # Удаление ветки в удалённом репо
```

### Работа с коммитами
```sh
git add .                      # Добавление всех изменений в индекс

git commit -m "Commit message"  # Фиксация изменений

git commit -am "Commit message" # Добавление и коммит в одной команде

git push origin 'nameBranch'   # Отправка изменений в удалённый репозиторий
```

### Слияние изменений
```sh
git merge 'nameBranch'         # Слияние указанной ветки в текущую

git merge --continue           # Продолжение процесса слияния

git merge --abort              # Отмена слияния

git branch -d 'NameBranch'     # Удаление ветки после слияния
```

### Работа с историей
```sh
git fetch                      # Получение данных без слияния

git reset <file>               # Удаление файла из индекса

git reset HEAD~n --soft        # Откат n коммитов, сохраняя изменения

git reset HEAD~n --hard        # Откат n коммитов, удаляя изменения

git restore --staged <file>    # Удаление файла из индекса без удаления изменений

git commit --amend             # Изменение последнего коммита

git push origin main --force   # Перезапись истории (ОСТОРОЖНО!)

git cherry-pick <hash>         # Применение одного коммита в текущей ветке
```

---

## Решение конфликтов
```sh
git checkout main
git pull
git checkout 'nameBranch'
git merge main  # Попытка слить изменения
```

### Если есть конфликты:
1. Разрешить конфликты в файлах.
2. Добавить исправленные файлы:
   ```sh
   git add .
   git merge --continue
   ```

---

## Общая схема работы с Git
```plaintext
Working Directory  -> Staging Area -> Local Repo -> Remote Repo
    |                   |                 |             |
    |  git add         ->|  git commit   ->| git push  ->|
    |                   |                 |             |
    |  <- git checkout |                 |<- git clone |
    |  <- git pull     |                 |             |
    |                 <- git fetch       |             |
```

---

## Проблема: Расхождения между локальной и удалённой веткой
```sh
git status
git diff main origin/main  # Сравнение локальных и удалённых изменений
```

