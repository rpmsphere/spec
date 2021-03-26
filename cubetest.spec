Name: cubetest
Summary: CubeTest
Version: 0.9.4
Release: 1
License: GPL v2
URL:     http://www.vandenoever.info/software/cubetest/
Group:   Amusements/Games/Logic
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}.desktop
Source2: %{name}.png
BuildRequires: qt4-devel

%description
This program was written for a competition from Linux Magazine. The competition
was held because of a lack of good educational software for primary schools.
The program CubeTest is aimed at primary school students. With it, you can train
your spatial insight.

vraagMost people know the type of question: a cube is shown together with four
alternatives. The objective is to point out the cube that is identical to the
one shown. The cubes from which you can choose are oriented differently from
the first cube and one has to turn the cubes mentally in order to decide which
ones are the same.

These question are a great way of improving your spatial insight. This is a
valuable asset in many technical areas. In adition it's just plain fun to
answer these questions and no matter how often you practice, they never become
really easy.

%prep
%setup -q

%build
cp -f /usr/share/automake-*/config.guess .
pushd src/object
moc-qt4 side.h -o side_moc.cpp
moc-qt4 object.h -o object_moc.cpp
cd ../fun
moc-qt4 fun.h -o fun_moc.cpp
cd ../cubetest
moc-qt4 testdialog.h -o testdialog_moc.cpp
moc-qt4 cube.h -o cube_moc.cpp
moc-qt4 scorekeeper.h -o scorekeeper_moc.cpp
moc-qt4 cubedialog.h -o cubedialog_moc.cpp
popd
QT_INCLUDE_DIR="/usr/include/QtCore" QT_CXXFLAGS="-I/usr/include/QtCore/ -I/usr/include/QtGui -I/usr/include/xulrunner-sdk-1.9/system_wrappers -I/usr/include/Qt3Support" ./configure --with-qt --prefix=%{_prefix}
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall

#install Desktop & icons
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -fr %buildroot

%files
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_bindir}/fun
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
* Mon Nov 03 2008 Feather Mountain <john@ossii.com.tw>
- Rebuild for M6(OSSII)
* Sun May 11 2008 Dominique Leuenberger <dominique-rpm@leuenberger.net>
- Initial package for OBS, Version 0.9.4
