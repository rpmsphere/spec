%global debug_package %{nil}

Name: smillaenlarger
Summary: Graphical tool to resize bitmaps in high quality
Version: 0.9.0
Release: 5.1
License: GPLv3+
Group: Amusements/Graphics
URL: http://sourceforge.net/projects/imageenlarger/
Source0: smillaenlarger_%{version}.orig.tar.bz2
Source1: smillaenlarger_%{version}-0.2~ppa3.debian.tar.bz2
BuildRequires: qt-devel gcc-c++ desktop-file-utils

%description
SmillaEnlarger is a small graphical tool (based on Qt) to resize,
especially magnify bitmaps in high quality.

%prep
%setup -q -a 1
patch -p1 < debian/patches/fix_version.diff
cd SmillaEnlargerSrc
qmake-qt4 ImageEnlarger.pro

%build
cd SmillaEnlargerSrc
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -D SmillaEnlargerSrc/SmillaEnlarger %{buildroot}%{_libexecdir}/SmillaEnlarger
%{__install} -m0644 -D SmillaEnlargerSrc/smilla.png %{buildroot}%{_datadir}/pixmaps/smillaenlarger.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications debian/etc/smillaenlarger.desktop

#%{__install} -m0755 -D debian/etc/smillaenlarger %{buildroot}%{_bindir}/smillaenlarger
# (^^;
sed -i -e 's|/usr/share/doc/smillaenlarger|%{_docdir}/%{name}-%{version}|g' \
       -e 's|/usr/lib/smillaenlarger|%{_libexecdir}|g' debian/etc/smillaenlarger
%{__install} -m0755 -D debian/etc/smillaenlarger %{buildroot}%{_bindir}/smillaenlarger

%clean
%{__rm} -rf %{buildroot}

%files
%doc ReadMe.rtf WhatsNew.rtf changelog.txt gpl-3.0.txt
%doc debian/etc/smillaenlarger.ini
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.0
- Rebuild for Fedora
* Wed Apr 11 2012 Sawa <sawa@ikoinoba.net> - 0.9.0
- Initial package
