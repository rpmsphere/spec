%global debug_package %{nil}

Summary: Commodore BASIC V2 as a scripting language
Name: cbmbasic
Version: 2.0
Release: 5.1
License: BSD
Group: Development/Languages
Source: %{name}-master.zip
URL: https://github.com/mist64/cbmbasic

%description
"Commodore BASIC" (cbmbasic) is a 100% compatible version of Commodore's
version of Microsoft BASIC 6502 as found on the Commodore 64. You can use
it in interactive mode or pass a BASIC file as a command line parameter.

%prep
%setup -q -n %{name}-master

%build
export CC="gcc -Wl,--allow-multiple-definition"
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files 
%doc *.md test/*
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Mar 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
