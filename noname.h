///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Aug 22 2019)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/panel.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class NamaNorma
///////////////////////////////////////////////////////////////////////////////
class NamaNorma : public wxFrame
{
	private:

	protected:
		wxPanel* m_panel1;
		wxStaticText* m_staticText1;
		wxStaticText* m_staticText2;
		wxTextCtrl* m_textCtrl_nama_norma;
		wxButton* m_button_ok;
		wxButton* m_button_batal;

		// Virtual event handlers, overide them in your derived class
		virtual void m_button_okOnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void m_button_batalOnButtonClick( wxCommandEvent& event ) { event.Skip(); }


	public:

		NamaNorma( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Binakarir"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,100 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~NamaNorma();

};

