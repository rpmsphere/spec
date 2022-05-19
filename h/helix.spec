%undefine _debugsource_packages

Name:           helix
Version:        22.03
Release:        1
Summary:        A post-modern modal text editor written in Rust
License:        Apache-2.0, MIT, BSD-3-Clause, BSL-1.0, Zlib, MPL-2.0
URL:            https://github.com/helix-editor/helix
Source0:        %{name}-%{version}~0.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        helix.sh
Source4:        helix-rpmlintrc
Source5:        README.SUSE
BuildRequires:  cargo

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation.

%prep
%autosetup -a1 -n %{name}-%{version}~0
mkdir -p .cargo
cp %{SOURCE2} .cargo/config
cp %{SOURCE5} docs/README.SUSE

%build
#export RUSTFLAGS="-Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2"
# We must disable fetching and building the treesitter grammars because this is a limitation with OBS cargo-packaging for now
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=true
cargo build --release --locked --offline

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}/runtime
install -m 0755 target/release/hx %{buildroot}%{_libexecdir}/%{name}/hx
cp -rv "runtime/queries" %{buildroot}%{_libexecdir}/%{name}/runtime
cp -rv "runtime/themes" %{buildroot}%{_libexecdir}/%{name}/runtime
install -Dm644 runtime/tutor.txt -t %{buildroot}%{_libexecdir}/%{name}/runtime
install -D -d -m 0755 %{buildroot}%{_bindir}
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md docs/README.SUSE CHANGELOG.md languages.toml docs/CONTRIBUTING.md docs/architecture.md docs/vision.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 22.03
- Rebuilt for Fedora
* Sun May  1 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- remove home-in-%%post filter in helix-rpmlintrc
- fix LICENSE string
* Fri Apr 22 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- fix build errors
* Fri Apr 22 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- copy README.SUSE to doc
* Thu Apr 21 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- change to %%{SOURCE4} in %%doc section
* Thu Apr 21 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- add README.SUSE
- remove %%post message from spec file
* Thu Apr 21 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- add helix-rpmlintrc:
  * filters duplicate errors
  * filters home in %%post errors when actually it is just a message
* Thu Apr 21 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- fix potential bashism in rpmlint
* Wed Apr 20 2022 Soc Virnyl Estela <socvirnyl.estela@gmail.com>
- Initial spec for helix (22.03~0)
