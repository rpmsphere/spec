Name: pac
Summary: Perl Auto Connector
Version: 4.5.5.7
Release: 1
Group: Converted/networking
License: GPLv3
URL: https://sites.google.com/site/davidtv/
Source0: https://sourceforge.net/projects/pacmanager/files/pac-4.0/%{name}-%{version}-all.tar.gz
BuildRequires:  desktop-file-utils
BuildArch: noarch
Requires: ftp
Requires: perl(Carp)
Requires: perl(Crypt::CBC)
Requires: perl(Crypt::Rijndael)
Requires: perl(Digest::SHA)
Requires: perl(DynaLoader)
Requires: perl(Encode)
Requires: perl(Expect)
Requires: perl(Exporter)
Requires: perl(File::Basename)
Requires: perl(File::Copy)
Requires: perl(FindBin)
Requires: perl(Gnome2::GConf)
Requires: perl(Gtk2)
Requires: perl(Gtk2::Ex::Simple::List)
Requires: perl(Gtk2::Ex::Simple::TiedCommon)
Requires: perl(Gtk2::GladeXML)
Requires: perl(IO::Socket::INET)
Requires: perl(KeePass)
Requires: perl(Net::ARP)
Requires: perl(Net::Ping)
Requires: perl(OSSP::uuid)
Requires: perl(PACCluster)
Requires: perl(PACConfig)
Requires: perl(PACEdit)
Requires: perl(PACExecEntry)
Requires: perl(PACExpectEntry)
Requires: perl(PACGlobalVarEntry)
Requires: perl(PACKeePass)
Requires: perl(PACMain)
Requires: perl(PACMethod)
Requires: perl(PACPCC)
Requires: perl(PACPipe)
Requires: perl(PACPrePostEntry)
Requires: perl(PACScreenshots)
Requires: perl(PACScripts)
#Requires: perl(PACShell)
Requires: perl(PACStatistics)
Requires: perl(PACTermOpts)
Requires: perl(PACTerminal)
Requires: perl(PACTray)
Requires: perl(PACTree)
Requires: perl(PACUtils)
Requires: perl(PACVarEntry)
Requires: perl(POSIX)
Requires: perl(Socket)
Requires: perl(Socket6)
Requires: perl(Storable)
Requires: perl(Sys::Hostname)
Requires: perl(TiedTree)
Requires: perl(Time::HiRes)
Requires: perl(YAML)
Requires: perl(constant)
Requires: perl(lib)
Requires: perl(strict)
Requires: perl(vars)
Requires: perl(warnings)
Requires: perl-Crypt-Blowfish
Requires: perl-Crypt-Rijndael
Requires: perl-IO-Stty
Requires: perl-Gnome2-Vte
Requires: telnet
Requires: vte

%description
Gnome's SecureCRT/Putty/blah blah... equivalent (on steroids!) written in Perl/GTK.
PAC is a telnet/ssh/rsh/etc connection manager/automator written in Perl GTK
aimed at making both administrators and switchers (from Windoze) live easier.

%prep
%setup -q -n %{name}
rm -rf lib/ex/vte*

%build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a lib res utils %{buildroot}%{_datadir}/%{name}

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5.5.7
- Rebuilt for Fedora
* Fri Dec 14 2012 David Torrejon Vaquerizas
- Initial package
