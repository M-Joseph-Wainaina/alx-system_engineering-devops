class flask_install {
  package { 'python3-pip':
    ensure => installed,
  }
  
  exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    path    => ['/usr/bin'],
    unless  => '/usr/bin/pip3 show flask | grep "Version: 2.1.0"',
  }
}

include flask_install
