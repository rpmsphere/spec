%global debug_package %{nil}

Name: kconfigure
Summary: KDE tool for Building and installing software from source
Version: 2.1
Release: 11.1
License: GPL
Group: Graphical desktop/KDE
Source: %name-%version.tar.bz2
URL: http://kconfigure.sourceforge.net
BuildRequires: libpng-devel qt3-devel libstdc++-devel xorg-x11-proto-devel zlib-devel subst arts-devel libjpeg-devel
BuildRequires: freetype-devel gcc-c++ kde-settings kdebase3-devel kdelibs3-devel desktop-file-utils
BuildRequires: libsmbclient-devel libwbclient-devel

%description
Kconfigure simplifies the automake/checkinstall process by offering a simplified GUI interface.
Easy to use, click the configure file in Konqueror and configure, make and install the sources from
within kconfigure.  Features include checkinstall support (for creating RPM, Slackware, and DKPG
installation files), Qmake support, HTML or plaintext logging, Konqueror integration, and a helpful
configure option dialog.

%prep
%setup -q
subst 's,\.la\>,.so,' configure
sed -i 's|false) == 4|0) == 4|' kconfigure/kconfigure.cpp

%build
%configure \
    --disable-debug \
    --enable-final \
    --disable-rpath \
    --prefix=%_prefix
%__make CXXFLAGS="-fpermissive -fPIC" -j

%install
%__make install DESTDIR=$RPM_BUILD_ROOT

# menu
cat > kconfigure.desktop <<EOF
[Desktop Entry]
Name=KConfigure
GenericName=KConfigure
Comment=KDE tool for Building and installing software from source
Exec=kconfigure
Terminal=false
Icon=kconfigure
Type=Application
Encoding=UTF-8
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install                                     \
        --vendor ""                                      \
        --add-category Development                       \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications    \
        kconfigure.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%_bindir/*
%_mandir/*
%exclude %_datadir/applnk/Applications/*
%_datadir/apps/*
%_datadir/applications/*
%_datadir/doc/*
%_datadir/mimelnk/*
%_datadir/icons/*

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Tue Oct 04 2005 X-Stranger <xstranger@altlinux.ru> 2.1-alt2
- rpath disabled
* Fri Jul 29 2005 X-Stranger <xstranger@altlinux.ru> 2.1-alt1
- built for ALT Linux
