%undefine _debugsource_packages

Name:          lvsgsp
Version:       0.0.4
Release:       4.1
Summary:       Linux Virtual Server Global Stats Processor
Group:         System/Servers
URL:           https://www.linuxvirtualserver.org/~acassen/
Source:        https://www.linuxvirtualserver.org/~acassen/software/lvsgsp-%{version}.tar.gz
License:       BSD

%description
The goal of this software is to provide a graphical tracking system for an LVS
realserver pool activity. Using this tool, an administrator can track eventual
realserver overload activity that provide key decision to increase LVS realserver pool.

%prep
%setup -q

%build
make %{_smp_mflags} INCLUDE=

%install
sed -i "s|/usr/local/bin|$RPM_BUILD_ROOT%{_bindir}|" Makefile
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make install 
chmod 755 %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/lvsgsp

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4
- Rebuilt for Fedora
* Thu Sep 27 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.0.4-2mamba
- specfile fixes for openmamba
* Thu Jun 17 2004 Silvan Calarco <silvan.calarco@qilinux.it> 0.0.4-1qilnx
- first build
