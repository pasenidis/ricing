# i3 Bar

## How?

Just set a script that loops the execution of this status bar.

Don't know how?

```sh
#!/bin/sh

cd path/to/bar
while :
do
  	python main.py
    sleep 1
done
```

Also, don't forget to set the .sh script in the i3 config (usually located at `~/.config/i3/config`).

```sh
bar {
    status_command ./bar.sh
}
```
