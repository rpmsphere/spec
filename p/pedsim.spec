Name: pedsim
Version: 2.3
Release: 3.1
Summary: A Microscopic Pedestrian Crowd Simulation System 
License: GPLv3
Group: Development/Libraries
URL: http://pedsim.silmaril.org/
Source0: http://pedsim.silmaril.org/dist/libpedsim/20140211-libpedsim-2-3-src.tar.gz
BuildRequires: qt-devel

%description
PEDSIM is a microscopic pedestrian crowd simulation system. It is suitable for
use in crowd simulations (e.g. indoor evacuation simulation, large scale outdoor
simulations), where one is interested in output like pedestrian density or
evacuation time. Also, the quality of the individual agent's trajectory is high
enough for creating massive pedestrian crowd animations (e.g. for motion pictures
or architectural visualization). Since libpedsim is easy to use and extend, it is
a good starting point for science projects.

%prep
%setup -q -c
sed -i 's|QtWidgets|QtGui|' demoapp/src/mainwindow.cpp

%build
make -C libpedsim
cd demoapp
qmake-qt4
make

%install
install -Dm755 lib%{name}/lib%{name}.so %{buildroot}%{_libdir}/lib%{name}.so
install -Dm755 demoapp/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
* Wed Feb 12 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Rebuild for Fedora
