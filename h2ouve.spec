#undefine __arch_install_post
#undefine _missing_build_ids_terminate_build
%global debug_package %{nil}
%global kversion %(uname -r)

Summary: 	Insyde Variable Editor
Name: 		h2ouve
Version: 	200.01.00.10
Release: 	1.bin
License: 	Commercial, freeware
Group:		Development/Tools
Source0:	InsydeH2OUVE_x86_LINUX64_portable_%{version}.tar.bz2
Source1:        %{name}-README.txt
Source2:        %{name}-ReleaseNotes.txt
Source3:	insydeh2o.png
URL:		http://www.insyde.com/
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Requires:	kernel = %(uname -r|sed 's/-.*//')

%description
Insyde Variable and SCU Editor Utility for Linux.

%prep
%setup -q -c
#sed -i '25i #include <linux/sched.h>' driver/phy_alloc.c
cp %{SOURCE1} README.txt
cp %{SOURCE2} ReleaseNotes.txt

%build
cd driver
make

%install
mkdir -p %{buildroot}/usr/lib/insyde
cp -a gui isbiosmem h2ouve-l* locales %{buildroot}/usr/lib/insyde
mkdir -p %{buildroot}/usr/lib/insyde/driver
cp driver/*.ko %{buildroot}/usr/lib/insyde/driver
mkdir -p %{buildroot}/usr/lib/insyde/runtime/misc
cp %{SOURCE3} %{buildroot}/usr/lib/insyde/runtime/misc
mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/insyde/h2ouve-lx64 %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Insyde H2OUVE™
Comment=H2O Variable and SCU Editor
Exec=h2ouve -g
Icon=/usr/lib/insyde/runtime/misc/insydeh2o.png
Terminal=false
Categories=System;Settings;Utility;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%{_bindir}/%{name}
/usr/lib/insyde
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Oct 28 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 200.01.00.10
- Initial package
