%global debug_package %{nil}

Name:           gnushogi
Version:        1.4.2
Release:        10.1
Group:          Amusements/Games
Summary:        The game of Shogi, also known as Japanese Chess
License:        GPLv3+
URL:            http://www.gnu.org/software/%{name}
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
GNU shogi is a program that plays shogi, the Japanese version of chess,
against a human (or computer) opponent. This is only the AI engine, and
you will likely want to use a GUI front-end (xshogi or xboard) to be
more comfortable.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}
make -C gnushogi gnushogi.bbk

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=%{buildroot}%{_prefix}
# v1.4.2 tend to drop docs in /usr instead of /usr/share
mkdir -p %{buildroot}%{_datarootdir}
if [ ! -d %{buildroot}%{_infodir} ] ; then
    mv %{buildroot}%{_prefix}/info %{buildroot}%{_infodir}
fi
if [ ! -d %{buildroot}%{_libdir} ] ; then
    mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
fi
if [ ! -d %{buildroot}%{_mandir} ] ; then
    mv %{buildroot}%{_prefix}/man %{buildroot}%{_mandir}
fi

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_infodir}/%{name}.*
%{_libdir}/%{name}
%{_mandir}/man6/%{name}.*

%changelog
* Mon Jul 31 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.2
- Rebuild for Fedora
* Thu Jul 17 2014 Chen Chen <aflyhorse@hotmail.com> 1.4.2-1
- Initial version of the package
