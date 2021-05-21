Name:           alacritty
Version:        0.5.0
Release:        1
Summary:        A cross-platform, GPU-accelerated terminal emulator
Group:          Terminals
License:        ASL 2.0
URL:            https://github.com/jwilm/alacritty
Source0:        https://github.com/jwilm/alacritty/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        alacritty-cargo-vendor-%{version}.tar.xz
Source2:        cargo.config
Source4:	https://github.com/jwilm/alacritty/releases/download/v%{version}/Alacritty.svg
# This is the script that creates the Source1 tar-ball needed to build without net access.
# Update the version here and then run the script.
# You need to have the "vendor" package for cargo installed.
# To install: urpmi cargo-vendor
Source100:      pack-cargo-vendor.sh
BuildRequires:  cargo
BuildRequires:  cmake
BuildRequires:  freetype-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  desktop-file-utils
Requires(post): ncurses
Requires(post): ncurses-extraterms
Requires:       xclip
Recommends:     tmux

%description
Alacritty is focused on simplicity and performance. The performance goal means
it should be faster than any other terminal emulator available. The simplicity
goal means that it doesn't have features such as tabs or splits (which can be
better provided by a window manager or terminal multiplexer) nor niceties
like a GUI config editor.

The software is considered to be at an alpha level of readiness - there are
missing features and bugs to be fixed, but it is already used by many as a
daily driver.

%package zsh-completion
Summary:        A cross-platform, GPU-accelerated terminal emulator
Group:          Terminals
BuildArch:      noarch
Requires:       zsh
Requires:       %{name} >= %{version}-%{release}

%description zsh-completion
This is the shell completion for ZSH.

%package bash-completion
Summary:        A cross-platform, GPU-accelerated terminal emulator
Group:          Terminals
BuildArch:      noarch
Requires:       bash
Requires:       %{name} >= %{version}-%{release}

%description bash-completion
This is the shell completion for BASH.

%package fish-completion
Summary:        A cross-platform, GPU-accelerated terminal emulator
Group:          Terminals
BuildArch:      noarch
Requires:       fish
Requires:       %{name} >= %{version}-%{release}

%description fish-completion
This is the shell completion for FISH.

%package docs
Summary:        A cross-platform, GPU-accelerated terminal emulator
Group:          Terminals
BuildArch:      noarch
Requires:       %{name} >= %{version}-%{release}

%description docs
The documentation for %{name}.

%prep
%autosetup -a1 -p1

%build
%__mkdir .cargo
cp %{SOURCE2} .cargo/config

cargo build --release --verbose
cargo doc --verbose

%install
%__mkdir_p %{buildroot}%{_bindir}
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install -m755 extra/logo/*svg %{buildroot}%{_datadir}/icons
%__install -m755 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps
%__install -m755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
%__install -m644 extra/linux/Alacritty.desktop %{buildroot}%{_datadir}/applications

# Shell completions
%__mkdir_p %{buildroot}%{_datadir}/zsh/site-functions/
%__mkdir_p %{buildroot}%{_datadir}/bash-completion/completions/
%__mkdir_p %{buildroot}%{_datadir}/fish/completions/
%__mkdir_p %{buildroot}%{_mandir}/man1
%__mkdir_p %{buildroot}%{_docdir}/%{name}
cp extra/completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
cp extra/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
cp extra/completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
%__install -Dm 0644 extra/%{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
%__install -Dm 0644 extra/%{name}.info %{buildroot}%{_docdir}/%{name}/%{name}.info

rm -vf %{buildroot}%{_prefix}/.crates.toml

%post
echo "        Adding %{name} info to terminfo"
tic -e alacritty,alacritty-direct %{_docdir}/%{name}/%{name}.info > /dev/null 2>&1

%files
%license LICENSE-APACHE
%doc README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/Alacritty.svg
%{_docdir}/%{name}/%{name}.info
%{_datadir}/icons/%{name}*svg
%{_mandir}/man1/%{name}.1*

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%{_datadir}/fish/completions/%{name}.fish

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%files docs
%doc target/doc/alacritty/

%changelog
* Fri Aug 21 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuilt for Fedora
* Sat Jun 29 2019 kekepower <kekepower> 0.3.3-1.mga8
+ Revision: 1415902
- Update to version 0.3.3
* Sat May 11 2019 kekepower <kekepower> 0.3.2-3.mga7
+ Revision: 1397283
- Rebuild for new Rust
* Sat Apr 27 2019 kekepower <kekepower> 0.3.2-2.mga7
+ Revision: 1395741
- Use default config for alacritty (alacritty.yml)
* Tue Apr 23 2019 kekepower <kekepower> 0.3.2-1.mga7
+ Revision: 1394931
- Update to version 0.3.2
* Mon Apr 22 2019 kekepower <kekepower> 0.3.1-1.mga7
+ Revision: 1394748
- Update to version 0.3.1
* Tue Apr 09 2019 kekepower <kekepower> 0.3.0-1.mga7
+ Revision: 1387233
- Update to version 0.3.0
* Wed Feb 13 2019 kekepower <kekepower> 0.2.9-1.mga7
+ Revision: 1366504
- Update to version 0.2.9
* Sun Feb 10 2019 kekepower <kekepower> 0.2.8-1.mga7
+ Revision: 1365156
- Update to version 0.2.8
* Sat Jan 26 2019 kekepower <kekepower> 0.2.7-2.mga7
+ Revision: 1361079
- Remove patch now that llvm has been fixed
* Mon Jan 21 2019 kekepower <kekepower> 0.2.7-1.mga7
+ Revision: 1359066
- Update to version 0.2.7
- Add patch to disable building with lto enabled
 o This is due to a bug or regression in either Rust or LLVM
 o See https://github.com/rust-lang/rust/issues/57762
* Tue Jan 08 2019 kekepower <kekepower> 0.2.5-1.mga7
+ Revision: 1351560
- Update to versoin 0.2.5
* Tue Dec 18 2018 kekepower <kekepower> 0.2.4-3.mga7
+ Revision: 1342489
- Requires ncurses-extraterms
* Fri Dec 14 2018 kekepower <kekepower> 0.2.4-2.mga7
+ Revision: 1341254
- Fixed font issue
* Fri Dec 14 2018 kekepower <kekepower> 0.2.4-1.mga7
+ Revision: 1341220
- imported package alacritty
