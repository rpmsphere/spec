Summary: File Service Protocol Client
Name: fspclient
Version: 0.93.1
Release: 2
Group: System Environment/Daemons
License: BSD/MIT/X
URL: https://fspclient.sourceforge.net
Source0: %{name}-%{version}.tar.bz2
BuildRequires: glibc-devel python2-scons sed

%description
FSP client with FTP-like interface.

%prep
%setup -q

%build
scons prefix=%{buildroot}%_prefix \
      mandir=%{buildroot}%_mandir \
      docdir=%{buildroot}/not-used

%install
scons prefix=%{buildroot}%_prefix \
      sysconfdir=%_sysconfdir \
      mandir=%{buildroot}%_mandir \
      docdir=%{buildroot}/not-used \
      install
#     --install-sandbox=%{buildroot}
rm -rf %{buildroot}/not-used

%files
%doc doc/FOR.MORE.INFO README fsprc ChangeLog
%{_bindir}/fsp
%{_mandir}/man?/fsp.*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.93.1
- Rebuilt for Fedora
* Sat Aug 24 2019 Radim Kolar <hsn@sendmail.cz>
- Initial packaging
