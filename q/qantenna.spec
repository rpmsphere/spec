Name:		qantenna
Version:	0.3.0
Release:	1
Summary:	Software dedicated to viewing and analyzing antennas
Group:		Sciences/Physics 
License:	GPLv2
#URL:		https://qantenna.sourceforge.net/
#Source0:	https://downloads.sourceforge.net/project/qantenna/qantenna/%{version}/%{name}-%{version}.tar.bz2
#Source0:	https://sourceforge.net/projects/qantenna/files/qantenna/0.3.0/qantenna-0.3.0.orig.tar.xz
URL:		https://github.com/groleo/qantenna
Source0:	%{name}-master.zip
Patch0:		qantenna-0.2.3-mdv-link.patch
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	qt5-qtbase-devel
BuildRequires:	mesa-libGL-devel

%description
QAntenna is a FLOSS software dedicated to viewing and analizing
antennas and their radiation patterns. It provides the user with a
3D view of the models, capable of zooming, rotating, and more to come.

%prep
%setup -q -n %{name}-master
%patch0 -p1
#sed -i 's|static const float runDelta= 0.04;|static constexpr float runDelta= 0.04;|' src/camera.h
#sed -i 's|static const float zoomStep= 0.1;|static constexpr float zoomStep= 0.1;|' src/glwidget.h
#sed -i 's|static const float sensibility= 0.1;|static constexpr float sensibility= 0.1;|' src/glwidget.h

%build
qmake-qt5 PREFIX=/usr qantenna.pro
make RPM_OPT_FLAGS="%{optflags}"

%install
make INSTALL_ROOT=%{buildroot} install
install -m644 README.md THANKS TODO BUGS AUTHORS ChangeLog COPYING %{buildroot}%{_datadir}/doc/%{name}

%files
%{_datadir}/doc/%{name}
%{_bindir}/qantenna

%changelog
* Sun Jul 02 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuilt for Fedora
* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 770399
+ rebuild (emptylog)
* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.3-1
+ Revision: 770365
- update to 0.2.3
* Fri Dec 03 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 605788
- import qantenna
