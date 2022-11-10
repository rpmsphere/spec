%global debug_package %{nil}
%global __arch_install_post %{nil}
%undefine _missing_build_ids_terminate_build

Summary: 	Insyde Flash Firmware Tool
Name: 		h2offt
Version: 	200.02.00.06
Release: 	1.bin
License: 	Commercial, freeware
Group:		Development/Tools
Source0:	InsydeH2OFFT_x86_LINUX64_%{version}.tar.bz2
URL:		http://www.insyde.com/
BuildRequires:  kernel-headers
BuildRequires:  kernel-devel
Requires:	kernel = %(uname -r|sed 's/-.*//')

%description
The linux tool to flash BIOS firmware.

%prep
%setup -q -n InsydeH2OFFT_x86_LINUX64_%{version}
#sed -i 's|uname -m|uname -i|' driver/Makefile         
#sed -i '25i #include <linux/sched.h>' driver/phy_alloc.c
sed -i '/MODULE_SUPPORTED_DEVICE/d' driver/phy_alloc.c

%build
cd driver
make

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -R *.ini Logo.png driver/*.ko %{buildroot}%{_libexecdir}/%{name}
cp h2offt h2offt-g %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
if [ \$# -eq 0 ] ; then
ARGS="-h"
else
ARGS="\$(realpath \$1)"
shift
ARGS+=" \$*"
fi
cd /usr/libexec/%{name}
if [ -z "\$DISPLAY" ] ; then
./h2offt \$ARGS
else
./h2offt-g \$ARGS
fi
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ReleaseNotes.txt
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Sun Nov 13 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 200.02.00.06
- Update package
