Name:               gigaset-frontend
Version:            0.6.0
Release:            15.1
Summary:            Siemens Gigaset configuration software
Source:             http://prdownloads.sourceforge.net/gigaset307x/gigaset-frontend-%{version}.tar.gz
Source1:            gigaset-frontend.desktop
Patch1:             gigaset-frontend-optflags.patch
Patch2:             gigaset-frontend-fix_uninitialized.patch
Source2:            gigaset.png
URL:                http://gigaset307x.sourceforge.net/frontend.html
Group:              Hardware/ISDN
License:            GNU General Public License version 2 (GPLv2)
BuildRequires:      libpng-devel
BuildRequires:      kernel-devel
BuildRequires:      glibc-devel
BuildRequires:      kernel-headers
BuildRequires:      qt4-devel
BuildRequires:      expat-devel
BuildRequires:      gcc gcc-c++ make glibc-devel pkgconfig

%description
This package contains user space configuration programs for Siemens Gigaset
ISDN devices.

%package qt
Summary:            Siemens Gigaset configuration software (GUI)
Group:              Hardware/ISDN

%description qt
This package contains qgigaset, a graphical user space configuration program
for Siemens Gigaset ISDN devices.

%prep
%setup -q
%patch1
%patch2

%build
# not autotools:
./configure \
    --prefix="%{_prefix}" \
    --libdir="%{_libdir}" \
    --mandir="%{_mandir}" \
    --datadir="%{_datadir}" \
    --destdir="$RPM_BUILD_ROOT" \
    --with-expat \
    --with-qt \
    --without-qtlibs

%__make %{?_smp_flags} \
    RELEASE=1 \
    CC="%__cc" \
    CXX="%__cxx" \
    OPTFLAGS="%{optflags}" \
    QTDIR="%{_usr}" \
    QTBINDIR="%{_libdir}/qt4/bin"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__make \
    RELEASE=1 \
    CC="%__cc" \
    CXX="%__cxx" \
    OPTFLAGS="%{optflags}" \
    QTDIR="%{_usr}" \
    QTBINDIR="%{_libdir}/qt4/bin" \
    DESTDIR="$RPM_BUILD_ROOT" \
    install

find "$RPM_BUILD_ROOT%{_datadir}/" -type f -exec %__chmod -x {} \;

LFILE="$PWD/.lang"
pushd "$RPM_BUILD_ROOT%{_datadir}/qgigaset"
/bin/ls -1d *.qm | while read qm; do
    l="${qm##*_}"
    l="${l%.qm}"
    echo "%lang($l) %{_datadir}/qgigaset/$qm" >>"$LFILE"
done

%__install -D -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
%__install -D -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/gigaset.png

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc COPYING README TODO Release.notes known_bugs.txt
%{_sbindir}/gigaconf
%{_sbindir}/gigacontr
%doc %{_mandir}/man8/gigaconf.8.*
%doc %{_mandir}/man8/gigacontr.8.*

%files qt -f .lang
%{_bindir}/qgigaset
%{_datadir}/qgigaset
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/gigaset.png
##%exclude %{_libdir}/libQt*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.0
- Rebuilt for Fedora
* Sun Aug 21 2011 pascal.bleser@opensuse.org
- initial version (0.6.0)
