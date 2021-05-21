Name:			antargis
Summary:		Battles of Antargis is a medieval-like realtime strategy game
URL:			http://antargis.berlios.de/
Group:			Amusements/Games/Strategy/Real Time
Version:		0.2.1.5
Release:		1295
License:		GPL
BuildRequires:	gcc-c++
BuildRequires:	libpng-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	ruby-devel
BuildRequires:	rubygem-rake
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	swig
BuildRequires:	zip
Requires:		ruby
Source0:		%{name}.tar.bz2

%description
Battles of Antargis is a medieval-like realtime strategy game.

You are a hero who was betrayed and you have to unify the kingdom
and rebuild the old empire. Old myths will pass your way.

The game is currently in heavy development and taking up pace.
The current features include:
* A short tutorial giving you an introduction to the gameplay
* Beginning of a real campaign

Antargis gives you the opportunity to strive through the land,
conquer villages, build new ones, recruit troops and finally
defeat your enemies. Your people have their own mind, so you
will have to care for them. Otherwise they'll turn against you.
And you have only a small bunch of heroes to do your job. Your
mission awaits you...

%prep
%setup -q -n %{name}

%__sed -i -e 's|Gem::Platform::LINUX_586|Gem::Platform::CURRENT|g' Rakefile
%__sed -i -e 's|1.3.33|1.3.40|g' rookey/lib/rookey/configs/swig.rb

%__rm data/gui/antargis.icns

%__sed -i '1i #include <typeinfo>' ext/*/*.cc
%__sed -i '1i #include <algorithm>' ext/3dengine/*.cc ext/game/map.cc
%__sed -i '1i #include <cstdlib>' ext/basic/ag_rand_base.cc rookey/lib/rookey/cpp/rk_tools.cc


%build
rake

%install
%__install -dm 755 %{buildroot}%{_libdir}/%{name}
%__install -m 755 %{name} \
	%{buildroot}%{_libdir}/%{name}
%__install -m 644 %{name}.so \
	%{buildroot}%{_libdir}/%{name}

%__install -dm 755 %{buildroot}%{_datadir}/games/%{name}
%__install -m 644 *.rb \
	%{buildroot}%{_datadir}/games/%{name}
%__cp -a data \
	%{buildroot}%{_datadir}/games/%{name}
%__cp -a ruby \
	%{buildroot}%{_datadir}/games/%{name}
%__install -dm 755 %{buildroot}%{_datadir}/games/%{name}/rookey
%__cp -a rookey/lib \
	%{buildroot}%{_datadir}/games/%{name}/rookey
pushd %{buildroot}%{_datadir}/games/%{name}
	ln -s %{_libdir}/%{name}/%{name} .
	ln -s %{_libdir}/%{name}/%{name}.so .
popd

# install start script
%__install -dm 755 %{buildroot}%{_bindir}
%__cat > %{name} << EOF
#!/bin/sh

cd %{_datadir}/games/%{name}
./%{name} "\$@"
EOF
%__install -m 755 %{name} \
	%{buildroot}%{_bindir}

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 data/gui/portraits/Godrin.png \
	%{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu-entry
%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=Battles of Antargis is a medieval-like realtime strategy game
Name=Battles of Antargis
GenericName=Battles of Antargis
Type=Application
Exec=%{name}.sh
Icon=%{name}
Categories=Game;StrategyGame;
EOF

# rpmlint is yelling :)
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/antargisStarter.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/checktabs.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/editor.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/ant_application.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/credits.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/editor_app.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/intro.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/map_generator2.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/mesh_view.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/obj_import.rb
%__chmod 644 %{buildroot}%{_datadir}/games/%{name}/ruby/spec_helper.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/test_ant3.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/editor/test/player_dialog.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/gui/ag_tools.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tests/*.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tests/path/heuristic_test.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tests/path/fields_test.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tests/path/fields_test2.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tools/ant2obj.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tools/anim_import.rb
%__chmod 755 %{buildroot}%{_datadir}/games/%{name}/ruby/tools/anim_import4.rb

# cleanup's
%__rm -r %{buildroot}%{_datadir}/games/%{name}/rookey/lib/rookey/cpp
%__rm -r %{buildroot}%{_datadir}/games/%{name}/rookey/lib/rookey/swig


%clean
%__rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/%{name}
%{_libdir}/%{name}/%{name}.so
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}*.desktop

# writable for group games
%defattr(-,root,games,775)
%dir %{_datadir}/games/%{name}

# group games
%defattr(-,root,games,755)
%{_datadir}/games/%{name}/%{name}
%{_datadir}/games/%{name}/%{name}.so
%{_datadir}/games/%{name}/*.rb
%dir %{_datadir}/games/%{name}/ruby
%{_datadir}/games/%{name}/ruby/README
%{_datadir}/games/%{name}/ruby/*.rb
%dir %{_datadir}/games/%{name}/ruby/ai
%{_datadir}/games/%{name}/ruby/ai/README
%{_datadir}/games/%{name}/ruby/ai/*.rb
%{_datadir}/games/%{name}/ruby/ai/*.txt
%dir %{_datadir}/games/%{name}/ruby/ai/spec
%{_datadir}/games/%{name}/ruby/ai/spec/*.rb
%dir %{_datadir}/games/%{name}/ruby/debugging
%{_datadir}/games/%{name}/ruby/debugging/README
%dir %{_datadir}/games/%{name}/ruby/editor
%{_datadir}/games/%{name}/ruby/editor/*.rb
%dir %{_datadir}/games/%{name}/ruby/editor/campaign
%{_datadir}/games/%{name}/ruby/editor/campaign/*.rb
%dir %{_datadir}/games/%{name}/ruby/editor/spec
%{_datadir}/games/%{name}/ruby/editor/spec/*.rb
%dir %{_datadir}/games/%{name}/ruby/editor/test
%{_datadir}/games/%{name}/ruby/editor/test/*.rb
%dir %{_datadir}/games/%{name}/ruby/entities
%{_datadir}/games/%{name}/ruby/entities/README
%{_datadir}/games/%{name}/ruby/entities/*.rb
%dir %{_datadir}/games/%{name}/ruby/entities/spec
%{_datadir}/games/%{name}/ruby/entities/spec/*.rb
%dir %{_datadir}/games/%{name}/ruby/gui
%{_datadir}/games/%{name}/ruby/gui/*.rb
%dir %{_datadir}/games/%{name}/ruby/jobs
%{_datadir}/games/%{name}/ruby/jobs/README
%{_datadir}/games/%{name}/ruby/jobs/*.rb
%dir %{_datadir}/games/%{name}/ruby/jobs/spec
%{_datadir}/games/%{name}/ruby/jobs/spec/*.rb
%dir %{_datadir}/games/%{name}/ruby/meshes
%{_datadir}/games/%{name}/ruby/meshes/*.rb
%dir %{_datadir}/games/%{name}/ruby/multiplayer
%{_datadir}/games/%{name}/ruby/multiplayer/README
%dir %{_datadir}/games/%{name}/ruby/spec
%{_datadir}/games/%{name}/ruby/spec/*.rb
%dir %{_datadir}/games/%{name}/ruby/spec/story
%{_datadir}/games/%{name}/ruby/spec/story/story_spec
%{_datadir}/games/%{name}/ruby/spec/story/*.rb
%dir %{_datadir}/games/%{name}/ruby/scripting
%{_datadir}/games/%{name}/ruby/scripting/README
%dir %{_datadir}/games/%{name}/ruby/state_machine
%{_datadir}/games/%{name}/ruby/state_machine/*.rb
%dir %{_datadir}/games/%{name}/ruby/state_machine/spec
%{_datadir}/games/%{name}/ruby/state_machine/spec/*.rb
%dir %{_datadir}/games/%{name}/ruby/state_machine/tests
%{_datadir}/games/%{name}/ruby/state_machine/tests/*.rb
%dir %{_datadir}/games/%{name}/ruby/tests
%{_datadir}/games/%{name}/ruby/tests/*.rb
%dir %{_datadir}/games/%{name}/ruby/tests/3d_engine
%{_datadir}/games/%{name}/ruby/tests/3d_engine/*.rb
%dir %{_datadir}/games/%{name}/ruby/tests/path
%{_datadir}/games/%{name}/ruby/tests/path/*.rb
%dir %{_datadir}/games/%{name}/ruby/tools
%{_datadir}/games/%{name}/ruby/tools/*.rb
%dir %{_datadir}/games/%{name}/ruby/widgets
%{_datadir}/games/%{name}/ruby/widgets/*.rb

%dir %{_datadir}/games/%{name}/rookey
%dir %{_datadir}/games/%{name}/rookey/lib
%{_datadir}/games/%{name}/rookey/lib/*.rb
%dir %{_datadir}/games/%{name}/rookey/lib/rookey
%{_datadir}/games/%{name}/rookey/lib/rookey/*.rb
%dir %{_datadir}/games/%{name}/rookey/lib/rookey/configs
%{_datadir}/games/%{name}/rookey/lib/rookey/configs/*.rb
#%dir %{_datadir}/games/%{name}/rookey/lib/rookey/cpp
#%{_datadir}/games/%{name}/rookey/lib/rookey/cpp/*
#%dir %{_datadir}/games/%{name}/rookey/lib/rookey/swig
#%{_datadir}/games/%{name}/rookey/lib/rookey/swig/*

#%defattr(644,root,games,755)
%dir %{_datadir}/games/%{name}/data
%{_datadir}/games/%{name}/data/*.png
%{_datadir}/games/%{name}/data/*.xml
%dir %{_datadir}/games/%{name}/data/campaigns
%{_datadir}/games/%{name}/data/campaigns/*.xml
%dir %{_datadir}/games/%{name}/data/fonts
%{_datadir}/games/%{name}/data/fonts/*.ttf
%dir %{_datadir}/games/%{name}/data/gui
%{_datadir}/games/%{name}/data/gui/*.png
%{_datadir}/games/%{name}/data/gui/*.svg
%{_datadir}/games/%{name}/data/gui/*.xcf
%dir %{_datadir}/games/%{name}/data/gui/campaign
%{_datadir}/games/%{name}/data/gui/campaign/*.png
%{_datadir}/games/%{name}/data/gui/campaign/*.xcf
%dir %{_datadir}/games/%{name}/data/gui/editor
%{_datadir}/games/%{name}/data/gui/editor/*.png
%{_datadir}/games/%{name}/data/gui/editor/*.svg
%dir %{_datadir}/games/%{name}/data/gui/editor/entities
%{_datadir}/games/%{name}/data/gui/editor/entities/*.png
%dir %{_datadir}/games/%{name}/data/gui/images
%dir %{_datadir}/games/%{name}/data/gui/images/basic
%{_datadir}/games/%{name}/data/gui/images/basic/*.png
%{_datadir}/games/%{name}/data/gui/images/basic/*.svg
%dir %{_datadir}/games/%{name}/data/gui/layout
%{_datadir}/games/%{name}/data/gui/layout/*.xml
%dir %{_datadir}/games/%{name}/data/gui/layout/editor
%dir %{_datadir}/games/%{name}/data/gui/layout/editor/campaign
%{_datadir}/games/%{name}/data/gui/layout/editor/campaign/*.xml
%dir %{_datadir}/games/%{name}/data/gui/portraits
%{_datadir}/games/%{name}/data/gui/portraits/*.png
%{_datadir}/games/%{name}/data/gui/portraits/*.svg
%{_datadir}/games/%{name}/data/gui/portraits/*.xcf
%dir %{_datadir}/games/%{name}/data/gui/svg
%{_datadir}/games/%{name}/data/gui/svg/*.svg
%dir %{_datadir}/games/%{name}/data/levels
%{_datadir}/games/%{name}/data/levels/*.png
%dir %{_datadir}/games/%{name}/data/levels/ai
%dir %{_datadir}/games/%{name}/data/levels/birth
%{_datadir}/games/%{name}/data/levels/birth/*.hmap
%{_datadir}/games/%{name}/data/levels/birth/*.rb
%dir %{_datadir}/games/%{name}/data/levels/dev
%{_datadir}/games/%{name}/data/levels/dev/*.png
%{_datadir}/games/%{name}/data/levels/dev/*.rb
%dir %{_datadir}/games/%{name}/data/levels/multiplayer
%dir %{_datadir}/games/%{name}/data/levels/tutorial
%{_datadir}/games/%{name}/data/levels/tutorial/*.hmap
%{_datadir}/games/%{name}/data/levels/tutorial/*.rb
%dir %{_datadir}/games/%{name}/data/local
%{_datadir}/games/%{name}/data/local/*.txt
%dir %{_datadir}/games/%{name}/data/models
%{_datadir}/games/%{name}/data/models/*
%dir %{_datadir}/games/%{name}/data/music
%{_datadir}/games/%{name}/data/music/*.ogg
%dir %{_datadir}/games/%{name}/data/shaders
%{_datadir}/games/%{name}/data/shaders/*.frag
%{_datadir}/games/%{name}/data/shaders/*.vert
%dir %{_datadir}/games/%{name}/data/sound
%{_datadir}/games/%{name}/data/sound/*.wav
%dir %{_datadir}/games/%{name}/data/textures
%{_datadir}/games/%{name}/data/textures/*.png
%{_datadir}/games/%{name}/data/textures/*.xcf
%dir %{_datadir}/games/%{name}/data/textures/2d
%{_datadir}/games/%{name}/data/textures/2d/*.png
%dir %{_datadir}/games/%{name}/data/textures/2d/terrain
%{_datadir}/games/%{name}/data/textures/2d/terrain/*.png
%{_datadir}/games/%{name}/data/textures/2d/terrain/*.xcf
%dir %{_datadir}/games/%{name}/data/textures/models
%{_datadir}/games/%{name}/data/textures/models/*.png
%{_datadir}/games/%{name}/data/textures/models/*.tga
%{_datadir}/games/%{name}/data/textures/models/*.xcf
%dir %{_datadir}/games/%{name}/data/textures/splats
%{_datadir}/games/%{name}/data/textures/splats/*.png
%{_datadir}/games/%{name}/data/textures/splats/*.xcf
%dir %{_datadir}/games/%{name}/data/textures/terrain
%{_datadir}/games/%{name}/data/textures/terrain/*.jpg
%{_datadir}/games/%{name}/data/textures/terrain/*.png
%{_datadir}/games/%{name}/data/textures/terrain/*.rb
%{_datadir}/games/%{name}/data/textures/terrain/*.sh
%{_datadir}/games/%{name}/data/textures/terrain/*.xcf
%dir %{_datadir}/games/%{name}/data/tips
%{_datadir}/games/%{name}/data/tips/*.txt

# saved game data, writable for group games
%defattr(664,root,games,775)
%{_datadir}/games/%{name}/data/levels/*.antlvl
%{_datadir}/games/%{name}/data/levels/birth/*.antlvl
%{_datadir}/games/%{name}/data/levels/dev/*.antlvl
%{_datadir}/games/%{name}/data/levels/multiplayer/*.antlvl
%{_datadir}/games/%{name}/data/levels/tutorial/*.antlvl

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Mar 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1.5-1.ossii
- Rebuild for OSSII
* Fri Feb 27 2009 Toni Graffy <toni@links2linux.de> - 0.2.1.5-1294.pm.svn20090227
- update to actual svn -r1294
- moved binaries to /usr/lib/antargis and data to /usr/share/games/antargis
* Fri Jan 04 2008 Toni Graffy <toni@links2linux.de> - 0.2.1.5-0.pm.1
- update to 0.2.1.5
- buildsystem switched to rake
- using fdupes
- patched for ruby-1.8
* Tue Nov 27 2007 Toni Graffy <toni@links2linux.de> - 0.2.1.4-0.pm.1
- initial build 0.2.1.4
