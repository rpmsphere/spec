Name: python3-mido
Summary: Python module for working with MIDI messages and ports
Version: 1.2.8
Release: 4.1
Group: python
License: Free Software
URL: https://pypi.python.org/pypi/mido
Source0: https://codeload.github.com/olemb/mido/tar.gz/1.2.8#/mido-%{version}.tar.gz
BuildRequires: python3-devel
BuildArch: noarch

%description
Mido has full support for the 18 messages defined by the MIDI standard.
Mido brings support for MIDI files (read, write, create and play) with
complete access to every message in the file, including all common meta
messages. Implements MIDI over TCP/IP with socket ports, allowing wireless MIDI
between two computers. Also includes programs for playing MIDI files, listing
ports and serving and forwarding ports over a network.

%prep
%setup -q -n mido-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc LICENSE README.rst
%{_bindir}/mido-*
%{python3_sitelib}/*

%changelog
* Fri Aug 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.8
- Rebuild for Fedora
