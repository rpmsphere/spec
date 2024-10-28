Summary:        A text-based subtitles editor
Name:           subtitlecomposer
Version:        0.5.7
#Version:       0.6.4
Release:        29.4
URL:            https://github.com/maxrd2/subtitlecomposer
Source0:        %{name}-%{version}.tar.gz
License:        GPLv2+
Group:          Applications/Multimedia
BuildRequires:  gcc-c++, kdelibs-devel
BuildRequires:  gstreamer1-devel, gstreamer1-plugins-base-devel
BuildRequires:  libicu-devel
BuildRequires:  qca2 grep udisks2

%description
A text-based subtitles editor that supports basic operations as well as more
advanced ones, aiming to become an improved version of Subtitle Workshop for
every platform supported by KDE.

%prep
%setup -q
sed -i '9i include_directories(%{_libdir}/gstreamer-1.0/include)' CMakeLists.txt
%if %{fedora}>23
sed -i 's|static const double MaxSeconds|static constexpr double MaxSeconds|' src/core/time.h
sed -i 's|log2(flag)|log2(float(flag))|' src/core/subtitleline.cpp
%endif

%build
%cmake
%cmake_build

%install
%__rm -rf $RPM_BUILD_ROOT
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog TODO
%{_bindir}/%{name}
%{_datadir}/kde4/apps/%{name}
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/config/%{name}rc
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Thu Oct 09 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.7
- Rebuilt for Fedora
* Mon Jul 02 2012 fwang <fwang> 0.5.3-2.mga3
+ Revision: 266620
- do not build xine backend
- fix more linkage
- link against x11
* Fri May 13 2011 ahmad <ahmad> 0.5.3-2.mga1
+ Revision: 97693
- Add a patch to fix the mimetypes installed by subtitlecompoer:
  o no need to duplicate the ones already available in the freedesktop specs
  o .txt files are not necessarily subtitles files
* Fri Apr 29 2011 ahmad <ahmad> 0.5.3-1.mga1
+ Revision: 93504
- imported package subtitlecomposer
