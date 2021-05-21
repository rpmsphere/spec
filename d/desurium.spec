Name:           desurium
Summary:        Desura open-source client
License:        GPL-3.0
Group:          Amusements/Games/Other
Version:        0.8.0rc10
#Version:        0.8.0rc11
Release:        2.1
URL:            https://github.com/lodle/Desurium
BuildRequires:  bison
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gperf
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  tinyxml-devel
BuildRequires:  unzip
BuildRequires:  v8-devel
BuildRequires:  yasm
BuildRequires:  gmock-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  c-ares-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
Requires:       bzip2
Requires:       curl
Requires:       libcef_desura
Source0:        Desurium-0.8.0_rc10.tar.bz2
Source1:        cef-291.tar.gz
Source2:        breakpad-850.tar.gz
Source3:        wxWidgets-2.9.3.tar.bz2
BuildRequires:  compat-gcc-34-c++

%description
This is the unbranded Open Source version of the Desura digital
games distribution client. It is a program that allows a user to
one click download and install games and modifications.

%prep
%setup -q -n Desurium-0.8.0_rc10
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
mkdir build
cd build
#cmake ..
#make
%cmake .. -DWITH_ARES=FALSE \
      -DWITH_FLASH=FALSE \
      -DCEF_URL="file://%{_sourcedir}/cef-291.tar.gz" \
      -DBREAKPAD_URL="file://%{_sourcedir}/breakpad-850.tar.gz" \
      -DWXWIDGET_URL="file://%{_sourcedir}/wxWidgets-2.9.3.tar.bz2" \
      -DRUNTIME_LIBDIR="%{_lib}/desurium" \
      -DDATADIR="share/desurium" \
      -DBUILD_CEF=FALSE -DBUILD_ONLY_CEF=FALSE -DDEBUG=OFF -DBUILD_TESTS=OFF \
      -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
      -DBINDIR="bin" \
      -DINSTALL_DESKTOP_FILE=ON \
      -DDESKTOPDIR="%{_datadir}/applications"

make

%install
cd build
%make_install

# RPM does not like spaces in filenames:
rm "%{buildroot}%{_datadir}/desurium/language/New Language Read Me.txt"

mkdir %{buildroot}%{_datadir}/pixmaps
cp %{buildroot}%{_datadir}/desurium/desura.png %{buildroot}%{_datadir}/pixmaps
desktop-file-edit --add-category="Amusement" \
                  --set-generic-name="Digital games distribution client" \
                  %{buildroot}%{_datadir}/applications/desura.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/pixmaps/desura.png
%{_datadir}/applications/desura.desktop
%{_datadir}/%{name}

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0rc10
- Rebuilt for Fedora
* Sun May 26 2013 mailaender@opensuse.org
- enable build of the CLI tools
* Sun Apr 28 2013 mailaender@opensuse.org
-  update to version 0.8.0_rc10
* Tue Mar 19 2013 mailaender@opensuse.org
- update the system MIME cache for desura:// links
* Sat Mar  9 2013 mailaender@opensuse.org
- update to version 0.8.0_rc9
- dropped flash video support
* Sun Feb 24 2013 mailaender@opensuse.org
- update to version 0.8.0_rc8
* Wed Feb  6 2013 mailaender@opensuse.org
- update to version 0.8.0_rc5
* Wed Jan 30 2013 mailaender@opensuse.org
- update to version 0.8.0_rc4
* Sun Aug 26 2012 mailaender@opensuse.org
- initial release
