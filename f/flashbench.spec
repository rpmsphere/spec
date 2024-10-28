Name:           flashbench
Version:        72
Release:        0
Summary:        Bench-marking and analysis utility for flash devices
License:        GPLv2
Group:          System/Kernel and hardware
URL:            https://github.com/bradfa/flashbench.git
#Source0:       %{name}-%{version}.tar.bz2
Source0:        %{name}-dev.zip

%description
Unfortunately flash manufacturers do not provide random speed, number of
open blocks and erase block size info, to help in deciding the optimum
partitioning strategy for a particular device.
Flashbench is a nice little command line application that can help in
finding this information for you, by checking the speeds achieved over
a range of settings. 
NOTE: This tool will cause loss of data on the device being tested and
should be used with caution. See:- /usr/share/doc/%{name}/README

%prep
%setup -q -n %{name}-dev

%build
make

%install
install -d -m 0755 %buildroot%{_bindir}
install -D -m 0755 erase %{buildroot}%{_bindir}
install -D -m 0755 %{name} %{buildroot}%{_bindir}

%files
%doc COPYING README
%{_bindir}/*

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 72
- Rebuilt for Fedora
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 71-alt1_1
- new version
