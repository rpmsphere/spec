Summary: File Service Protocol Daemon 
Name: fspd
Version: 2.8.1b29
Release: 2
Group: System Environment/Daemons
License: BSD/MIT/X
URL: https://fsp.sourceforge.net
Source0: fsp-%{version}.tar.bz2
Source1: fspd.init
BuildRequires: glibc-devel python2-scons flex

%description
FSP is a set of programs that implements a public-access
archive similar to an anonymous-FTP archive. It is not
meant to be a replacement for FTP; it is only meant to do
what anonymous-FTP does, but in a manner more acceptable
to the provider of the service and more friendly to the
clients.
FSP is UDP based and very useful on slow connections
and in a Wireless LAN.
This Package contains the fspd server program.

%prep
%setup -q -n fsp-%{version}

%build
scons prefix=%{buildroot}%_prefix \
      sysconfdir=%_sysconfdir \
      mandir=%{buildroot}%_mandir \
      docdir=%{buildroot}/not-used \
      without-clients=yes \
      without-fspscan=yes

%install
scons prefix=%{buildroot}%_prefix \
      sysconfdir=%_sysconfdir \
      mandir=%{buildroot}%_mandir \
      docdir=%{buildroot}/not-used \
      without-clients=yes \
      without-fspscan=yes \
      install
#     --install-sandbox=%{buildroot}
rm -rf %{buildroot}/not-used

# config file
mkdir -p %{buildroot}%{_sysconfdir}
cp -a fspd.conf %{buildroot}%{_sysconfdir}

#init script
mkdir -p %{buildroot}%{_sysconfdir}/rc.d/init.d
cp -a %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/fspd

%files
%doc BETA.README ChangeLog fspd.conf COPYRIGHT INFO INSTALL TODO
%config(noreplace) %{_sysconfdir}/fspd.conf
%{_bindir}/fspd
%{_mandir}/man?/fspd.*
%{_sysconfdir}/rc.d/init.d/fspd

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8.1b29
- Rebuilt for Fedora
* Sat Aug 24 2019 Radim Kolar <hsn@sendmail.cz>
- new upstream release 2.8.1b29
- tested on Centos 7
* Tue Jan 13 2004 Sven Hoexter <sven@wrack.telelev.de>
- new upstream release 2.8.1b19
* Tue Nov 18 2003 Sven Hoexter <sven@du-gehoerst-mir.de>
- new upstream release 2.8.1b17
- release should build with old flex versions
- fixed prob with condrestart in the postun scriptled
  it's not supported by the init script
* Sun Oct 26 2003 Sven Hoexter <sven@du-gehoerst-mir.de>
- changed the contents and names to the Debian naming scheme
- corrected my email address
* Sun Aug 24 2003 Sven Hoexter <sven@du-gehoerst-mir.de>
- Initial build.
