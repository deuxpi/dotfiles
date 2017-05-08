# frozen_string_literal: true

require 'English'

task default: :install

desc 'Install all packages and configuration files'
task install: %i(
  install:packages
  install:config
)

namespace :install do
  desc 'Install all packages'
  task packages: %i(linux_packages mac_packages)

  desc 'Install Homebrew'
  task :homebrew do
    next unless mac?
    next sh 'brew update' if homebrew?

    sh %{ruby -e "$(curl -fsSL
      https://raw.githubusercontent.com/Homebrew/install/master/install)"}
  end

  task :apt do
    next unless debian?

    sh 'sudo apt-get update'
  end

  task :common_packages do
    install_packages %w(
      ack
      bash-completion
      cmake
      git
      shellcheck
    )
  end

  task linux_packages: %i(apt common_packages) do
    next unless debian?

    install_packages %w(
      build-essential
      diceware
      ffmpeg
      firmware-linux
      firmware-linux-nonfree
      gnome
      ibus
      ibus-gtk3
      ibus-mozc
      ibus-wayland
      mpv
      powertop
      python-dev
      python3-dev
      tlp
      tmux
      vim-gtk3
      virtualenv
      xterm
    )
  end

  task mac_packages: %i(homebrew common_packages) do
    next unless mac?

    packages = %w(
      bash
      coreutils
      diffutils
      findutils
      fzf
      gnupg
      homebrew/dupes/grep
      moreutils
      python
      python3
    )
    packages << 'vim --override-system-vi'
    install_packages packages
  end

  desc 'Install configuration files'
  task :config do
    Dir.glob('misc/**') do |src|
      dest = File.join ENV['HOME'], ".#{File.basename(src)}"
      ln_s File.expand_path(src), dest if missing?(dest)
    end
  end
end

private

def mac?
  RUBY_PLATFORM =~ /darwin/
end

def linux?
  RUBY_PLATFORM =~ /linux/
end

def debian?
  `which apt-get` && $CHILD_STATUS.success?
end

def homebrew?
  `which brew` && $CHILD_STATUS.success?
end

def missing?(path)
  !(File.exist?(path) || File.symlink?(path))
end

def brew_installed?(package)
  package = package.split.first
  `brew list --versions #{package}` && $CHILD_STATUS.exitstatus.zero?
end

def install_packages(packages)
  packages = Array(packages)
  if debian?
    cmd = 'sudo apt-get install --no-install-recommends'
    sh "#{cmd} #{packages.join(' ')}"
  elsif homebrew?
    packages.reject { |package| brew_installed? package }.each do |package|
      sh "brew install #{package}"
    end
  end
end
