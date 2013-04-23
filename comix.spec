Summary: Comic book viewer
Name:    comix
Version: 4.0.4
Release: 3
License: GPLv2+
Group: Office
URL: http://comix.sourceforge.net/
Source: http://downloads.sourceforge.net/comix/%name-%{version}.tar.gz
Patch0: comix-4.0.0-disable-update-mime-db.patch

BuildArch: noarch
BuildRequires: python, python-imaging, jpeg-progs, pygtk2.0
BuildRequires: desktop-file-utils
Requires: python, python-imaging, jpeg-progs, pygtk2.0


%description
Comix is a comic book viewer. It reads zip, rar, tar, tar.gz, and tar.bz2
archives (often called .cbz, .cbr and .cbt) as well as normal image files.

%prep
%setup -q -n %{name}-%{version} 
%patch0 -p0

%build

%install
%{__install} -d %{buildroot}%{_prefix}
%{__python} install.py install --dir %{buildroot}%{_prefix}

%find_lang %{name} --with-gnome

desktop-file-install --vendor='' \
	--dir %buildroot%_datadir/applications \
	--remove-category='Application' \
	--add-category='GNOME;GTK' \
	%buildroot%_datadir/applications/*.desktop

%files -f %{name}.lang
%defattr(-, root, root)
%doc ChangeLog COPYING README
%{_bindir}/comicthumb
%{_bindir}/comix
%{_datadir}/comix
%{_mandir}/man1/*
%{_datadir}/applications/*comix.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/comix.xml


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 4.0.4-2mdv2011.0
+ Revision: 610153
- rebuild

* Fri Dec 11 2009 Jérôme Brenier <incubusss@mandriva.org> 4.0.4-1mdv2010.1
+ Revision: 476550
- new version 4.0.4
- drop Source1 (external icons unneeded, they are included in the source tarball)

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 4.0.3-2mdv2010.0
+ Revision: 437098
- rebuild

* Tue Mar 17 2009 Funda Wang <fwang@mandriva.org> 4.0.3-1mdv2009.1
+ Revision: 356612
- New version 4.0.3

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 4.0.2-1mdv2009.1
+ Revision: 324242
- New upstream release
- New upstream release 4.0.2

* Fri Dec 05 2008 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2009.1
+ Revision: 310747
- New version 4.0.0
- disable update mime db

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 3.6.4-3mdv2009.0
+ Revision: 240509
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu May 31 2007 Jérôme Soyer <saispo@mandriva.org> 3.6.4-1mdv2008.0
+ Revision: 33056
- New release


* Sun Apr 01 2007 Jérôme Soyer <saispo@mandriva.org> 3.6.3-1mdv2007.1
+ Revision: 150141
- New release
- New release 3.6.2

* Wed Dec 13 2006 Jérôme Soyer <saispo@mandriva.org> 3.6.1-1mdv2007.1
+ Revision: 96446
- New release 3.6.1

* Mon Nov 27 2006 Jérôme Soyer <saispo@mandriva.org> 3.6-1mdv2007.1
+ Revision: 87467
- Fix BuildRequires
- New release 3.6
- Import comix

* Sat Aug 26 2006 Lenny Cartier <lenny@mandriva.com> 3.5.1-1mdv2007.0
- 3.5.1

* Wed Aug 02 2006 Jerome Soyer <saispo@mandriva.org> 3.4-1mdv2007.0
- New release 3.4

* Mon Jul 17 2006 Jerome Soyer <saispo@mandriva.org> 3.3-1mdv2007.0
- New release 3.3

* Mon Jun 26 2006 Jerome Soyer <saispo@mandriva.org> 3.2.1-1mdv2007.0
- New release 3.2.1
- XDG Menu

* Thu Jun 15 2006 Jerome Soyer <saispo@mandriva.org> 3.2-1mdv2007.0
- New release 3.2

* Tue May 23 2006 Jerome Soyer <saispo@mandriva.org> 3.1.3-1mdk
- New release 3.1.3

* Fri May 19 2006 Jerome Soyer <saispo@mandriva.org> 3.1.2-1mdk
- New release 3.1.2

* Sat May 06 2006 Jerome Soyer <saispo@mandriva.org> 3.1-1mdk
- New release 3.1

* Sun Apr 16 2006 Jerome Soyer <saispo@mandriva.org> 3.0.1-1mdk
- New release 3.0.1

* Mon Apr 03 2006 Jerome Soyer <saispo@mandriva.org> 3.0-1mdk
- New release 3.0

* Tue Mar 21 2006 Jerome Soyer <saispo@mandriva.org> 2.9-1mdk
- First build
- Inspired from FC Dag Repos

