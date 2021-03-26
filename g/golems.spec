%define debug_package %{nil}
%define rev git20160603

Summary: 3D recreational physics simulator
Name: golems
Version: 0.57.1
Release: 12.1
License: GPLv3+
Group: Sciences/Physics
# http://sourceforge.net/projects/golems
URL: http://www.golemgame.com
BuildRequires: ant
BuildRequires: java-devel lua
Requires: jre >= 1.6.0
# git://golems.git.sourceforge.net/gitroot/golems/golems
Source0: %{name}-%{version}-%{rev}.zip
Source1: %{name}.desktop
Source2: %{name}
Patch0: %{name}-%{version}-mga-build.patch

%description
This is a most unusual game. There are no set objectives, and no way to “win”.
Golems is a 3D Physics and Artificial Intelligence Simulator, and you are
free to build anything that you would like, and watch it move realistically
according to Newton’s laws.
Build robots, spaceships, clocks, catapults or cannons. Add sensors, timers,
switches, motors. Give it a brain. Take the wheel and pilot your machine
yourself. Build anything.

%prep
%setup -q -n %{name}-%{version}-%{rev}
%patch0 -p1
# fix wrong-script-end-of-line-encoding
sed -i 's/\r//' ant/LICENSE ant/NOTICE
# fix spurious-executable-perm
chmod -x ant/COPYING ant/LICENSE ant/NOTICE

%build
pushd ant
export ANT_OPTS=-Dfile.encoding=UTF8
%ant
popd

%install
pushd ant/dist/Linux
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -af ./*.jar %{buildroot}%{_datadir}/%{name}/
rm -f ./lib/LICENSE ./lib/NOTICE
cp -af ./lib %{buildroot}%{_datadir}/%{name}/
popd
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE2} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -f ./dataFolder/com/golemgame/data/app/icons/golemIcon64.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc ant/COPYING ant/LICENSE ant/NOTICE
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jun 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.57.1-0.git20160603
- Rebuild for Fedora
* Fri Feb 26 2016 umeabot <umeabot> 0.57.1-0.git20140625.5.mga6
+ Revision: 979631
- Mageia 6 Mass Rebuild
* Thu Oct 29 2015 tv <tv> 0.57.1-0.git20140625.4.mga6
+ Revision: 896337
- disable debuginfo
- cannot be noarch
* Wed Jan 07 2015 alexl <alexl> 0.57.1-0.git20140625.4.mga5
+ Revision: 808895
- new desktop file
* Wed Oct 15 2014 umeabot <umeabot> 0.57.1-0.git20140625.3.mga5
+ Revision: 741970
- Second Mageia 5 Mass Rebuild
* Sun Sep 28 2014 umeabot <umeabot> 0.57.1-0.git20140625.2.mga5
+ Revision: 731468
- Mageia 5 Mass Rebuild
* Mon Jul 21 2014 alexl <alexl> 0.57.1-0.git20140625.1.mga5
+ Revision: 654928
- new snapshot
- updated launch script with according upstream
- added GenericName for desktop file
- fixed license in spec
- fixed Requires
- fixed rpmlint warnings (wrong-script-end-of-line-encoding and spurious-executable-perm)
- renamed build.patch
* Wed Jun 18 2014 alexl <alexl> 0.57.0-1.mga5
+ Revision: 637963
- imported package golems
