%global debug_package %{nil}
%global __brp_check_rpaths %{nil}

Summary: 	A GPU stress test and OpenGL benchmark
Name: 		gputest
Version: 	0.7.0
Release: 	1.bin
URL:		https://www.geeks3d.com/gputest/
License: 	freeware
Group:		Hardware/Tools
Source0:	https://ozone3d.net/gputest/dl/GpuTest_Linux_x64_%{version}.zip
Source1:	%{name}.sh
Source2:	%{name}.desktop
Source3:        %{name}.png
Requires:	python3-tkinter

%description
GpuTest comes with several GPU tests including some popular ones from Windows' world.
The number of GPU tests grows with the new versions of the tool. The following tests
are available in the latest version:
* FurMark: based stress test (OpenGL 2.1 or 3.2).
* TessMark: based tessellation test (OpenGL 4.0).
* GiMark: geometry instancing test (OpenGL 3.3).
* PixMark: Piano pixel shader test (OpenGL 2.1 or 3.2).
* PixMark: Volplosion pixel shader test (OpenGL 2.1 or 3.2).
* Plot3D: vertex shader test (OpenGL 2.1 or 3.2).
* Triangle: one of the most simple 3D scene ever made... (OpenGL 2.1 or 3.2).

%prep
%setup -q -n GpuTest_Linux_x64_%{version}
chmod -x *.sh

%build
2to3 -w %{name}_gui.py

%install
install -d %{buildroot}%{_libexecdir}/%{name}
cp -a * %{buildroot}%{_libexecdir}/%{name}
install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Nov 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.0
- Initial binary package
