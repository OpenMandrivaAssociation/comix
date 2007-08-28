%define name comix
%define version 3.6.4
%define summary Comic book viewer
%define title Comix

Summary: %summary
Name: %name
Version: %version
Release: %mkrel 1
License: GPL
Group: Office
URL: http://comix.sourceforge.net/
Source: http://dl.sf.net/comix/comix-%{version}.tar.bz2
Source1: %name-icons.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: python, python-imaging, jpeg-progs, pygtk2.0
Requires: python, python-imaging, jpeg-progs, pygtk2.0
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils


%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2 
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup -q -n %{name}-%{version} -a1

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_prefix}
%{__python} install.py install --installdir %{buildroot}%{_prefix}

%find_lang %{name} --with-gnome

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%{summary}
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Office;X-MandrivaLinux-Office-Publishing;
EOF

%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%post
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_desktop_database}
%{clean_mime_database}

%clean 
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog COPYING README
%doc %{_mandir}/man1/comicthumb.1*
%doc %{_mandir}/man1/comix.1*
%{_bindir}/comicthumb
%{_bindir}/comix
%{_datadir}/applications/*comix.desktop
%{_datadir}/icons/hicolor/48x48/apps/comix.png
%{_datadir}/pixmaps/comix.png
%{_datadir}/pixmaps/comix/
%{_iconsdir}/*/%name.png
%{_iconsdir}/%name.png
%{_datadir}/icons/hicolor/scalable/apps/%name.svg
%dir %{_datadir}/mime
%{_datadir}/mime/*


