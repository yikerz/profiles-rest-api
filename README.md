### Setting up your project

1. Initialize with git
2. Create file `.gitignore`
3. Create file `LICENSE` (optional)

### SSH linkage to GitHub

1. Generate ssh key ([cmd 1](#commands))
2. Add new ssh key on GitHub setting
3. Create new repo for this project

### Creating a development server

1. Initialize `ubuntu/bionic64` with Vagrant ([cmd 2](#commands))
2. Modify `Vagrantfile`
3. Create new VM ([cmd 3](#commands))
4. SSH to the Vagrant VM ([cmd 4](#commands))

### Commands

1. `ssh-keygen -t rsa -b 4096 -C "yikerz0425@gmail.com"`
2. `vagrant init ubuntu/bionic64`
3. `vagrant up`
4. `vagrant ssh`
