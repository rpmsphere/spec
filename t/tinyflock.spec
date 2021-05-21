Name: tinyflock
Summary: An interactive flocking demo
Version: 3.2git
Release: 14.1
Group: Amusement/Toys
License: MIT
URL: https://github.com/jakogut/tinyflock/releases
Source0: %{name}-master.zip
Source1: %{name}.png
BuildRequires: cmake
BuildRequires: gtest-devel
BuildRequires: libXrandr-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: freeglut-devel
BuildRequires: fann-devel
BuildRequires: glfw-devel

%description
A simple, high-performance, threaded, and interactive flocking demo written in C with GLFW.

%prep
%setup -q -n %{name}-master

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%cmake
%cmake_build

%install
cd %{_host}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=TinyFlock
Exec=%{name}
Terminal=false
Comment=An interactive flocking demo
Type=Application
Categories=Application;Graphics;
Icon=%{name}
EOF

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Feb 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2git
- Rebuilt for Fedora
