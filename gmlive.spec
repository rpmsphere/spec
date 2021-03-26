%global debug_package %{nil}

Summary:          Live video for linux
Name:             gmlive
Version:          0.22.3
Release:          11.1
URL:              http://code.google.com/p/gmlive/
License:          GPLv2
Group:	Applications/Multimedia
Source:           http://gmlive.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	  gmlive.desktop
BuildRequires:    libpng-devel
BuildRequires:    gcc-c++
BuildRequires:    intltool
BuildRequires:    gtkmm24-devel, cairomm-devel, glibmm24-devel, libglademm24-devel
Requires:	mplayer, sp-auth

%description
Live video for linux, maybe it is an UI for mplayer by playing live video.

%prep
%setup -q 
#sed -i '/warnDialog.run();/d' src/MainWindow.cpp

%build
export CXXFLAGS="-std=c++11 -fPIC"
%configure --disable-plugin --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

%{__install} -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/gmlive.desktop

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/gmlive
%{_datadir}/gmlive
%{_datadir}/applications/gmlive.desktop
%{_datadir}/locale/*/LC_MESSAGES/gmlive.mo
%{_datadir}/pixmaps/gmlive.png

%changelog
* Fri Jul 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.22.3
- Rebuild for Fedora
* Wed Aug 19 2009 Huang Wenlong <huangwenlong@redflag-linux.com> 0.21.2-3
-add patch gmlive-0.21.2-del-warndialog-for-sopcast.patch 
-del dialog for sopast 
* Thu Jul 09 2009 Wang Jizheng <jzwang@redflag-linux.com> 0.21.2-2
- remove Obsoletes: qsopcast
* Sat May 09 2009 Wang Jizheng <jzwang@redflag-linux.com> 0.21.2-1
- update to 0.21.2
* Mon Sep 1 2008 Xuqing Kuang <xqkuang@redflag-linux.com> - 0.20.3-1
- Initial build for Red Flag Desktop SP1
