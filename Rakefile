task default: %i[
  install_packages
  install_config
]

task install_packages: %i[
  install_common_packages
  install_linux_packages
]

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
  install_packages %w(bash-completion)
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
    cmd = 'apt-get install --no-install-recommends'
  elsif `which brew` && $?.success?
    cmd = 'brew install'
  end
  sh "sudo #{cmd} #{packages.join(' ')}"
end
