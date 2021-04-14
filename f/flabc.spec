Name: flabc
Summary: An editor for writing abc files
Version: 1.1.2
Release: 3.1
Group: Applications
License: GPL
URL: http://www.lautengesellschaft.de/cdmm/
Source0: http://www.lautengesellschaft.de/cdmm/%{name}-%{version}.tar.gz
BuildRequires: fltk-devel

%description
flabc is an editor for abc text files. For converting abc
files to postscript and midi it relies on the additional
external software abctab2ps and abc2midi.
2006-2010 by Christoph Dalitz

%prep
%setup -q
sed -i 's|-lstdc++|-lstdc++ -lX11|' src/Makefile

%build
make %{?_smp_mflags} -C src

%install
install -Dm755 src/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a templates examples %{buildroot}%{_datadir}/%{name}

%files
%doc README CHANGES LICENSE doc/*
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.2
- Rebuilt for Fedora
