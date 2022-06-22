%undefine _debugsource_packages

Name:           textadept
Version:        11.3
Release:        1
Summary:        A ridiculously fast and extensible text editor
URL:            http://foicica.com/textadept/
License:        MIT
Group:          Productivity/Editors/Other
Source0:        https://github.com/orbitalquark/textadept/archive/refs/tags/%{name}_%{version}.tar.gz#/%{name}-%{name}_%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  freetype-devel
BuildRequires:  readline-devel

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
%setup -q -n %{name}-%{name}_%{version}

%build
cd src
make deps
make
#make GTK3=1
make curses

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp -r core $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r lexers $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r modules $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r scripts $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -r themes $RPM_BUILD_ROOT%{_libdir}/%{name}
cp init.lua $RPM_BUILD_ROOT%{_libdir}/%{name}
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}
ln -s ../%{_lib}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 0755 %{name}-curses $RPM_BUILD_ROOT%{_libdir}/%{name}/%{name}-curses
ln -s ../%{_lib}/%{name}/%{name}-curses $RPM_BUILD_ROOT%{_bindir}/%{name}-curses
install -D -m 0644 core/images/ta_48x48.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%doc LICENSE README.md docs/*
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jun 5 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 11.3
- Rebuilt for Fedora
* Tue Jul 19 2011 dbuck@example.com
- initial SuSE release with version 3.9
