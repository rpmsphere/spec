%global debug_package %{nil}

Name:           textadept
Version:        6.6
#Version:        10.1
Release:        10.1
Summary:        A ridiculously fast and extensible text editor
URL:            http://foicica.com/textadept/
License:        MIT
Group:          Productivity/Editors/Other
Source:         http://foicica.com/textadept/download/%{name}_%{version}.src.zip
Source1:        %{name}.desktop
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  freetype-devel
BuildRequires:  readline-devel
Source2:        http://luajit.org/download/LuaJIT-2.1.0-beta3.tar.gz

%description
Textadept is a fast, minimalist, and ridiculously extensible text editor for
Linux, Mac OSX, and Windows. At its core lies less than 2000 lines of C code,
and that's how it always will be. While other editors rely on numerous plugins
for a wide range of functionality, recordable macros to speed up workflow, and
shell scripts to quickly transform text, Textadept takes it to the extreme:
it gives you complete control over the entire application using the embedded
Lua language. Lua is one of the fastest scripting languages available and has
a very small footprint. In fact, most of Textadept is written in Lua.

%prep
%setup -q -n %{name}_%{version}.src -a 2
sed -i 's|-rdynamic|-lgmodule-2.0 -rdynamic|' src/Makefile
rm -rf src/luajit
mv LuaJIT-2.1.0-beta3 src/luajit

%build
make -C src

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -r core $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r doc $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r lexers $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r modules $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r scripts $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r themes $RPM_BUILD_ROOT%{_libdir}/%{name}
cp init.lua $RPM_BUILD_ROOT%{_libdir}/%{name}
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}
ln -s %{_libdir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 0644 core/images/ta_48x48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc CHANGELOG.md FAQ.md LICENSE README.md THANKS.md doc/*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Oct 27 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 6.6
- Rebuild for Fedora
* Tue Jul 19 2011 dbuck@example.com
- initial SuSE release with version 3.9
