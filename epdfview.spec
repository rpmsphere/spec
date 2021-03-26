Summary: 	Simple PDF viewer using poppler without Gnome dependency
Name: 		epdfview
Version: 	0.1.8
Release: 	1
License:	GPL
URL: 		http://www.emma-soft.com/projects/epdfview/
Vendor:         OSS Integral Institute, Co., Ltd.
Source0: 	http://trac.emma-soft.com/epdfview/chrome/site/releases/%{name}-%{version}.tar.gz
Source1:	%{name}-0.1.7.zh_TW.po
Group: 		Applications/Productivity
Requires:	poppler >= 0.5.0, gtk2, poppler-glib
BuildRequires:  poppler-devel >= 0.5.0, gtk2-devel, poppler-glib-devel

%description
ePDFView is a free lightweight PDF document viewer using Poppler and GTK+ libraries.
The aim of ePDFView is to make a simple PDF document viewer, in the lines of Evince
but without using the Gnome libraries.
  
%prep
%setup -q
%{__cp} %{SOURCE1} po/zh_TW.po
msgfmt po/zh_TW.po -o po/zh_TW.gmo
echo "Name[zh_TW]=PDF 檢視器" >> data/epdfview.desktop
echo "Comment[zh_TW]=輕量級 PDF 文件檢視器" >> data/epdfview.desktop

%build
%configure
sed -i -e 's|-Werror=format-security|-Wno-format-security|' -e 's|-DHAVE_CONFIG_H|-DHAVE_CONFIG_H -D_IPP_PRIVATE_STRUCTURES|' Makefile */Makefile */*/Makefile
%__make

%install
%__rm -rf $RPM_BUILD_ROOT
%makeinstall
%__install -Dm 644 data/icon_epdfview-48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/icon_epdfview-48.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc README NEWS INSTALL COPYING AUTHORS 
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/epdfview/
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/pixmaps/*
%{_mandir}/man1/*

%changelog 
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.8
- Rebuild for Fedora
* Sat Jun 17 2006 - Bernhard Walle <bernhard@links2linux.de>
- new upstream version
* Sat May 13 2006 - Bernhard Walle <bernhard@links2linux.de>
- new upstream version: added find bar
* Wed Apr 26 2006 - Bernhard Walle <bernhard@links2linux.de>
- new upstream version
* Sun Apr 16 2006 - Bernhard Walle <bernhard@links2linux.de>
- initial package
