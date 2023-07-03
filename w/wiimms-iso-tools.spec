%undefine _debugsource_packages

Name:			wiimms-iso-tools
Summary:		A set of command line tools to manipulate WBFS containers
Version:		2.23a.r4534
Release:		4.1
License:		GPLv2
Group:			Applications/File
Source0:		wii-%{name}.tar.gz
URL:			https://wit.wiimm.de/
BuildRequires:	fuse-devel

%description
Wiimms ISO Tools is a set of command line tools to manipulate Wii and 
GameCube ISO images and WBFS containers. The tool-set consists of 
the following tools: wit, wwt, wdf, wfuse.

%prep
%setup -q -n %{name}

%build
make tools
make wfuse
make doc

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}/
install -m755 bin/wit bin/wwt bin/wdf bin/wfuse %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%doc doc/*.txt
%{_bindir}/*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.12git.4272
- Rebuilt for Fedora
