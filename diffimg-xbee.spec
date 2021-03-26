%global _name diffimg

Name: diffimg-xbee
Summary: Simple image comparison tool
Version: 2.3.0
Release: 1
Group: Applications/Multimedia
License: GPLv2
URL: http://sourceforge.net/projects/diffimg/
Source0: https://codeload.github.com/lingo/diffimg-xbee/tar.gz/%{version}-lingo#/diffimg-xbee-%{version}-lingo.tar.gz
BuildRequires: dos2unix
BuildRequires: qt4-devel
BuildRequires: qwt-devel
BuildRequires: opencv-devel
BuildRequires: cmake atlas

%description
DiffImg is a simple image comparison tool which take two images with the same
size as input. Some statitics are computed and the positions where pixel differ
are displayed as a color mask.

%prep
%setup -q -n %{name}-%{version}-lingo
#dos2unix tounix.sh
#sh ./tounix.sh
#sed -i 's|lib -lperceptualdiff|lib|' build/apps.pro
#sed -i 's|-lopencv_core|-lopencv_core -lopencv_imgcodecs -lperceptualdiff|' build/apps.pro
sed -i 's|opencv_core|opencv_core opencv_imgcodecs|' build/CMakeLists.txt

%build
cd build
#qmake-qt4 -recursive INSTALL_PREFIX=$RPM_BUILD_ROOT/usr %{name}.pro
%cmake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd build
#make install
%make_install
# remove doc
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{_name}
sed 's|%{buildroot}||' %{buildroot}%{_datadir}/applications/%{_name}.desktop > %{buildroot}%{_datadir}/applications/%{name}.desktop
sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mv %{buildroot}%{_bindir}/diffimg %{buildroot}%{_bindir}/diffimg-xbee
mv %{buildroot}%{_mandir}/man1/diffimg.1.gz %{buildroot}%{_mandir}/man1/diffimg-xbee.1.gz

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_mandir}/man*/*

%changelog
* Mon May 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.0
- Rebuild for Fedora
