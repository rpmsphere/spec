Name:           xshogi
Version:        1.4.2
Release:        2.1
Group:          Amusements/Games
Summary:        X Front-end of GNU Shogi
License:        GPLv3+
URL:            https://www.gnu.org/software/gnushogi
Source0:        https://ftp.gnu.org/gnu/gnushogi/%{name}-%{version}.tar.gz
BuildRequires:  libXt-devel, libXaw-devel
Requires:       gnushogi

%description
The (very) old frontend for the X Window system.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc AUTHORS BUGS ChangeLog COPYING NEWS README README.xboard
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.*

%changelog
* Mon Jul 31 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.2
- Rebuilt for Fedora
* Thu Jul 17 2014 Chen Chen <aflyhorse@hotmail.com> 1.4.2-1
- Initial version of the package
