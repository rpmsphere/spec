Name:				wiipresent
Version:			0.7.5.2
%define libwiimote_version 0.4
Release:			8.1
Summary:			Give Presentations with a Nintendo Wiimote
Source:        https://dag.wieers.com/home-made/wiipresent/wiipresent-%{version}.tar.bz2
# https://prdownloads.sourceforge.net/projects/libwiimote/libwiimote-%{libwiimote_version}.tgz
Source1:       libwiimote-%{libwiimote_version}.tar.bz2
Patch1:        libwiimote-optflags.patch
Patch2:        wiipresent-libwiimote_prefix.patch
Patch3:        libwiimote-newer_bluez.patch
URL:			   https://dag.wieers.com/home-made/wiipresent/
Group:			Hardware/Joystick
License:			GNU General Public License version 2 (GPL v2)
BuildRequires:	libX11-devel libXtst-devel
BuildRequires: bluez-libs-devel
BuildRequires:	gcc make glibc-devel
BuildRequires:	autoconf automake libtool

%description
WiiPresent is a small program that enables you to use a Nintendo Wiimote for
giving presentations using Open Office, xpdf, evince or Acrobat Reader. It was
designed as an off-the-shelf tool with no need to customize it.

Authors:
--------
    Dag Wieers <dag@wieers.com>
    Geerd-Dietger Hoffman <ribalba@gmail.com>

%prep
%setup -q -a 1
pushd "libwiimote-%{libwiimote_version}"
%patch1
%patch3
popd #"libwiimote-%{libwiimote_version}"
%patch2

%build
LIBWIIMOTE_PREFIX="$PWD/libwiimote-install"
pushd "libwiimote-%{libwiimote_version}"
[ -e ./configure ] || autoreconf -v

CFLAGS="%{optflags} -fPIC" \
CC="%__cc" \
./configure \
	 --prefix="$LIBWIIMOTE_PREFIX" \
	 --disable-shared \
	 --enable-static
# without -j:
%__make \
	 OPTFLAGS="%{optflags} -D_DISABLE_NONBLOCK_UPDATES" \
	 libwiimote_includedir="$LIBWIIMOTE_PREFIX/include"
%__make install \
	 libwiimote_includedir="$LIBWIIMOTE_PREFIX/include"
popd #"libwiimote-%{libwiimote_version}"
%__rm "$LIBWIIMOTE_PREFIX/lib"/lib*.so.*

%__make %{?jobs:-j%{jobs}} \
	 WIIMOTE_INC="-I${LIBWIIMOTE_PREFIX}/include" \
	 WIIMOTE_LIB="${LIBWIIMOTE_PREFIX}/lib/libcwiimote.a" \
	 lib="%{_lib}" \
	 CC="%__cc" \
	 CFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install \
	 prefix="%{_prefix}" \
	 sysconfdir="%{_sysconfdir}" \
	 bindir="%{_bindir}" \
	 datadir="%{_datadir}" \
	 mandir="%{_mandir}" \
	 lib="%{_lib}"

%__chmod 0644 wiipresent-xinit.sh

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc AUTHORS COPYING README TODO ChangeLog
%doc docs/*.html docs/*.txt
%doc wiipresent-xinit.sh
%{_bindir}/wiipresent
%{_datadir}/applications/wiipresent.desktop
%{_datadir}/pixmaps/wiipresent.svg
%{_mandir}/man1/wiipresent.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5.2
- Rebuilt for Fedora

* Mon Sep 14 2009 Pascal Bleser <pascal.bleser@opensuse.org> 0.7.5.2
- new package

# vim: set sw=3 ts=3 noet:
# Local Variables:
# mode: rpm-spec
# tab-width: 3
# End:
