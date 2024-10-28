%undefine _debugsource_packages
Name:           python-pushy
Version:        0.5.1
Release:        6.1
Summary:        Virtualenv-based automation of test activities
License:        MIT
Group:          Development/Languages/Python
URL:            https://awilkins.id.au/pushy
Source:         https://launchpad.net/pushy/0.5/0.5.1/+download/pushy-%{version}.zip
BuildRequires:  python-devel
BuildRequires:  python-paramiko
BuildRequires:  python-py
BuildRequires:  python-virtualenv
BuildRequires:  unzip
Requires:       python-argparse
Requires:       python-paramiko
Requires:       python-py
Requires:       python-virtualenv
Requires:       python-setuptools
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
The Pushy package provides applicaton developers with a simple interface for 
connecting two Python interpreters, either on the local host, or over a network. 
Once connected, the interpreters may access objects in each other, as if they 
were local. Where objects are mutable (i.e. may change over time), then objects 
are “proxied”. This means that a local object is created that mirrors the 
remote object, and sends all local function/attribute access calls to the 
remote object. Special care has been taken to proxy builtin types properly, 
so that proxied objects may be passed to Python’s various builtin functions.

Pushy contains multiple transports for connecting interpreters, as well as 
a means for users to provide their own transport modules. Builtin transports 
are provided for connecting to local interpreters, and to remote interpreters 
via SSH, named pipes (using SMB) on Microsoft Windows, and over plain old 
TCP/IP sockets (using daemon).

%prep
%setup -q -n pushy-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%{python2_sitelib}/*

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuilt for Fedora
* Sat Nov  3 2012 dkukawka@suse.com
- initial package
