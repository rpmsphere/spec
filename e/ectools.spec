Name: ectools
Summary: Energy Consumption Tools
Version: 0.2.2
Release: 25.1
Group: System/Tools
License: GPL
URL: https://github.com/cupertino/ectools
Source0: %{name}-master.zip
BuildRequires: boost-devel
BuildRequires: ncurses-devel

%description
Energy Consumption Tools (ectools) is an open source tools pack consisting of
a core library with sensors and power estimators, a data acquisition tool,
a monititoring tool and an energy profiler.

%prep
%setup -q -n %{name}-master
mkdir obj
sed -i 's|return ifile|return bool(ifile)|' src/libec/tools/Tools.cpp
sed -i 's|-Wall|-Wall -lpthread -std=gnu++98|' Makefile
sed -i -e '/float _value\[\];/d' -e '230i float _value[];' include/libec/sensor/SensorPidStat.h
%ifarch aarch64
sed -i '/cpuid.h/d' include/libec/device/CpuInfo.h
sed -i '/__cpuid/d' src/libec/controller/device/CpuInfo.cpp
%endif

%build
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m755 bin/ec* bin/valgreen %{buildroot}%{_bindir}

%files
%doc README gpl.txt
%{_bindir}/*

%changelog
* Fri Dec 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
