%undefine _debugsource_packages

Summary: Commodore BASIC V2 as a scripting language
Name: cbmbasic
Version: 5.0
Release: 1
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

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0
- Rebuilt for Fedora
