Name: torrtux
Summary: A terminal-program for downloading torrents from PirateBay
Version: 1.1.3
Release: 5.1
Group: Internet
License: GPLv3
URL: http://sourceforge.net/projects/torrtux/
Source0: http://sourceforge.net/projects/torrtux/files/Torrtux/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: perl-Switch
Requires: perl-libwww-perl
Requires: perl-AppConfig
Requires: xclip
Requires: perl-HTML-Parser
#Requires: perl-XML-RPC
Requires: perl-IO-Compress
#Requires: perl-appconfig

%description
Torrtux is a terminal-based program, written in perl for downloading
torrents from The Pirate Bay. If you live in a country where tpb is blocked
(UK, Fin, Be, Ne, etc), you can set a proxy in the config file.

%prep
%setup -q
sed -i -e '10,13d' -e '121,134d' install.pl

%build

%install
perl install.pl \
  --sharedir=%{buildroot}%{_datadir}/%{name} \
  --mandir=%{buildroot}%{_mandir}/man1/%{name}.1.gz \
  --scriptdir=%{buildroot}%{_bindir} \
  --docdir=%{buildroot}%{_datadir}/doc/%{name}-%{version}
cp .torrtuxrc %{buildroot}%{_datadir}/doc/%{name}-%{version}/torrtuxrc

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/doc/%{name}-%{version}

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.3
- Rebuild for Fedora
