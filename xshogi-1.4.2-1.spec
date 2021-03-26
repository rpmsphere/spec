Summary:        Japanese Version of Chess
Name:           xshogi
Version:        1.4.2
Release:        1
License:        GPL v2 or later
Group:          Amusements/Games/Board/Chess
URL:            ftp://ftp.gnu.org/pub/gnu/gnushogi/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.sig
Patch0:         %{name}-%{version}-aix.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-build

%description
Gnushogi plays a game of Japanese chess (shogi) against the user or it
plays against itself. Gnushogi is an modified version of the gnuchess
program. It has a simple alphanumeric board display or it can use the
xshogi program under the X Window System which is provided with this package..

Authors:
--------
    John Stanback, Matthias Mutz <mutz@fmi.uni-passau.de>


%prep
%setup -q
%patch0


%build
export CC=xlc_r

./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}

make %{?_smp_mflags}


%install
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install

/usr/bin/strip ${RPM_BUILD_ROOT}%{_bindir}/* || :

cd ${RPM_BUILD_ROOT}
mkdir -p usr/bin
cd usr/bin
ln -sf ../..%{_bindir}/* .


%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,system)
%doc BUGS NEWS README.xboard
%{_bindir}/*
%{_mandir}/man*/*
/usr/bin/*


%changelog
* Fri Mar 14 2014 Michael Perzl <michael@perzl.org> - 1.4.2-1
- first version for AIX V5.1 and higher
