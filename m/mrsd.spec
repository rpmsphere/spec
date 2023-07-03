%undefine _debugsource_packages

Name:           mrsd
Version:        0.2
Release:        1
Summary:        Chinese chess game
License:        GPLv2
Group:          Amusements/Games
URL:            https://ki11egg.sourceforge.net/
Source0:        https://ignum.dl.sourceforge.net/project/ki11egg/mrsd/0.2/mrsd-v0.2.tgz
Source1:        mrsd-0.2-fedora.tar.gz
Patch:          mrsd-0.2-fedora.patch
BuildRequires:  fltk-devel gcc-c++

%description
Chinese Chess (XiangQi) Sofware with strong AI.

%prep
%setup -q -n %{name}-v%{version} -a 1
%patch -p1
sed -i 's|-----MRSDdirectory-----|%{_libdir}/%{name}|g' mrsd mrsd.desktop
%ifarch aarch64
sed -i 's|-maccumulate-outgoing-args||' cfast7/Makefile
%endif
sed -i 's|FL/fl_file_chooser.H|FL/Fl_File_Chooser.H|' gcch/flt2.cc
sed -i '777s|<=0|==NULL|' gcch/flt2.cc

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/%{name}/img/
install -m 644 gcch/open.* ${RPM_BUILD_ROOT}%{_libdir}/%{name}/
install -m 755 gcch/xgcch ${RPM_BUILD_ROOT}%{_libdir}/%{name}/
install -m 644 gcch/client.sav ${RPM_BUILD_ROOT}%{_libdir}/%{name}/
install -m 644 gcch/*.icc ${RPM_BUILD_ROOT}%{_libdir}/%{name}/
install -m 644 gcch/img/* ${RPM_BUILD_ROOT}%{_libdir}/%{name}/img

install -m 755 -D mrsd ${RPM_BUILD_ROOT}%{_bindir}/mrsd
install -m 644 -D mrsd.desktop ${RPM_BUILD_ROOT}%{_datadir}/applications/mrsd.desktop

%clean
%__rm -rf %{buildroot}

%files 
%{_libdir}/%{name}
%{_bindir}/mrsd
%{_datadir}/applications/mrsd.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Mon Nov 12 2012 Robert Wei <robert.wei@ossii.com.tw> 0.2-1
- build RPM package for Fedora 17
