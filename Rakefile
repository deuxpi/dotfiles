task default: :install

task install: %i[
  install:packages
  install:config
]

namespace :install do
  def mac?
    RUBY_PLATFORM =~ /darwin/
  end

  def linux?
    RUBY_PLATFORM =~ /linux/
  end

  task :package_manager do
    Rake::Task['install:homebrew'].invoke if mac?
    Rake::Task['install:apt'].invoke if linux?
  end

  task :homebrew do
    if `which brew` && $?.success?
      sh 'brew update'
    else
      sh %Q{ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"}
    end
  end

  task :apt do
    sh "sudo apt-get update"
  end

  def all_packages
    subtasks = %i(common_packages)
    subtasks << :mac_packages if mac?
    subtasks << :linux_packages if linux?
    subtasks
  end

  task packages: all_packages

  task :common_packages do
    install_packages %w(ack git)
  end

  task :linux_packages do
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
      tlp
      tmux
      vim-gtk3
      virtualenv
      xterm
    )
  end

  task :mac_packages do
    packages  = %w(bash bash-completion coreutils diffutils findutils fzf gnupg2 homebrew/dupes/grep moreutils python python3)
    packages << 'vim --override-system-vi'
    install_packages packages
  end

  task :config do
    Dir.glob('misc/**') do |src|
      dest = File.join ENV['HOME'], ".#{File.basename(src)}"
      ln_s File.expand_path(src), dest unless File.exists?(dest) || File.symlink?(dest)
    end
  end

  def install_packages(packages)
    packages = Array(packages)
    if `which apt-get` && $?.success?
      cmd = 'sudo apt-get install --no-install-recommends'
      sh "#{cmd} #{packages.join(' ')}"
    elsif `which brew` && $?.success?
      packages.each do |package|
        if `brew list --versions #{package.split.first}` && $?.exitstatus == 1
          sh "brew install #{package}"
        end
      end
    end
  end
end
