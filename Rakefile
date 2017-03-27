task default: %i[
  install_packages
  install_config
]

def all_packages
  subtasks = %i(install_common_packages)
  subtasks << :install_mac_packages if RUBY_PLATFORM =~ /darwin/
  subtasks << :install_linux_packages if RUBY_PLATFORM =~ /linux/
  subtasks
end

task install_packages: all_packages

task :install_common_packages do
  install_packages %w(ack git)
end

task :install_linux_packages do
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

task :install_mac_packages do
  install_packages %w(bash bash-completion coreutils diffutils fzf gnupg2 grep python python3 vim)
end

task :install_config do
  Dir.glob('misc/**') do |src|
    dest = File.join ENV['HOME'], ".#{File.basename(src)}"
    if File.exists?(dest) || File.symlink?(dest)
      warn "#{dest} already exists"
    else
      ln_s File.expand_path(src), dest
    end
  end
end

def install_packages(packages)
  packages = Array(packages)
  if `which apt-get` && $?.success?
    cmd = 'sudo apt-get install --no-install-recommends'
    sh "#{cmd} #{packages.join(' ')}"
  elsif `which brew` && $?.success?
    packages.each do |package|
      if `brew list --versions #{package}` && $?.exitstatus == 1
        sh "brew install #{package}"
      end
    end
  end
end
